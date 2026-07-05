from app.analysis.repository.analyzer import (
    RepositoryAnalyzer,
)
from app.repository.models import (
    RepositoryAnalysisContext,
)
from app.repository.detector import RepositoryDetector
from app.repository.dependency_parser import (
    DependencyParser,
)
from app.repository.scanner import RepositoryScanner


class RepositoryAnalysisService:
    """
    High-level repository analysis service.

    Pipeline

    Repository
        ↓
    Scanner
        ↓
    Detector
        ↓
    Dependency Parser
        ↓
    LLM Repository Analyzer
    """

    def __init__(self):

        self.scanner = RepositoryScanner()

        self.detector = RepositoryDetector()

        self.dependencies = DependencyParser()

        self.analyzer = RepositoryAnalyzer()

    def get_summary(
        self,
        repository_path: str,
    ) -> str:
        """
        Returns an architectural summary of
        the repository.
        """

        directories, files = self.scanner.scan(
            repository_path
        )

        detection = self.detector.detect(
            repository_path,
            files,
        )

        dependency_list = self.dependencies.parse(
            repository_path
        )

        context = RepositoryAnalysisContext(
            repository_name=repository_path.split("/")[-1],
            repository_path=repository_path,
            language=detection.language,
            framework=detection.framework,
            package_manager=detection.package_manager,
            build_system=detection.build_system,
            entry_point=detection.entry_point,
            dependencies=dependency_list,
            directories=directories,
            files=files,
        )

        return self.analyzer.analyze(
            context
        )