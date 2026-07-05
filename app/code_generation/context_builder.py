from app.code_generation.jira_analyzer import JiraAnalyzer
from app.code_generation.repository_context import RepositoryAnalysisContext
from app.code_generation.models import (
    CodeGenerationContext,
    ContextDocument,
)
from app.services.jira.jira_service import JiraService
from app.rag.models import SearchRequest
from app.rag.service import RAGService
from app.analysis.repository_analyzer import RepositoryAnalysisService
from app.integrations.jira.models import GetIssueRequest
from app.workspace.service import WorkspaceService
from app.repository.repository_indexer import RepositoryIndexer
from app.repository.models import RepositoryIndexRequest
from app.workspace.models import PrepareWorkspaceRequest


class ContextBuilder:
    """
    Builds the complete context
    used for AI code generation.
    """

    def __init__(self):

        self.jira = JiraService()

        self.analyzer = JiraAnalyzer()

        self.repository = RepositoryAnalysisService()

        self.rag = RAGService()

        self.workspace = WorkspaceService()

        self.indexer = RepositoryIndexer()

    def build(
        self,
        repository: str,
        branch: str,
        jira_key: str,
    ) -> CodeGenerationContext:

        # -------------------------------------
        # Fetch Jira Story
        # -------------------------------------

        # issue = self.jira.get_issue(
        #     jira_key
        # )
        issue = self.jira.get_issue(
            GetIssueRequest(
                issue_key=jira_key
            )
        )

        # -------------------------------------
        # Analyze Story
        # -------------------------------------

        analysis = self.analyzer.analyze(
            issue
        )

        # -------------------------------------
        # Clone Repository
        # -------------------------------------
        workspace = self.workspace.prepare(
            PrepareWorkspaceRequest(
                repository=repository,
                branch=branch,
            )
        )

        # -------------------------------------
        # Repository Analysis
        # -------------------------------------
        # repository_summary = self.repository.get_summary(
        #     workspace.local_path
        # )

        # -------------------------------------
        # Index Repository into ChromaDB
        # -------------------------------------

        self.indexer.index_repository(
            RepositoryIndexRequest(
                repository=repository,
                branch=branch,
                local_path=workspace.local_path,
            )
        )

        repository_summary = self.repository.get_summary(
            workspace.local_path
        )

        # -------------------------------------
        # Semantic Search
        # -------------------------------------

        search = self.rag.search(
            SearchRequest(
                collection_name=repository,
                # query=analysis.summary,
                query=f"""
                    Jira Summary:
                    {analysis.summary}

                    Description:
                    {analysis.description}

                    Repository:
                    {repository}
                    """,
                top_k=5,
            )
        )

        documents = []

        for item in search.results:

            documents.append(
                ContextDocument(
                    file_path=item.metadata.get(
                        "file_path",
                        ""
                    ),
                    content=item.document,
                )
            )

        return CodeGenerationContext(

            repository=repository,

            branch=branch,

            repository_path=workspace.local_path,

            jira_key=jira_key,

            jira_summary=analysis.summary,

            jira_description=analysis.description,

            repository_summary=repository_summary,

            suggested_files=analysis.suggested_files,

            rag_documents=documents,
        )