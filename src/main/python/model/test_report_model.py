from jinja2 import Template, Environment, FileSystemLoader
from fbs_runtime.application_context.PyQt5 import ApplicationContext
import webbrowser, os
from model.learning_model import LearningModel
from model.project import Project

class TestReportModel:
    def __init__(self):
        appctxt = ApplicationContext()
        env = Environment(loader=FileSystemLoader(appctxt.get_resource('html/')))
        self.template = env.get_template('test_report_template.html')
        self.project = Project()
        self.test_results = LearningModel.default().test_results

    def generate_test_details(self):
        data = {
            'title': self.project.project_name(),
            'results': {
                'TP': self.test_results.true_positive,
                'FP': self.test_results.false_positive,
                'FN': self.test_results.false_negative,
                'TN': self.test_results.true_negative
            },
            'recall': round(self.test_results.recall * 100, 1),
            'precision': round(self.test_results.precision * 100, 1),
            'specificity': round(self.test_results.specificity * 100, 1)
        }
        html = self.template.render(data)
        return html
