from diagrams import Cluster, Diagram
from diagrams.programming.flowchart import InputOutput, Decision, Delay, Database, Document

with Diagram("Python If Then", show=False):
    input = InputOutput("input")
    decision = Decision("If Then")
    db = Database("Postgres")
    doc = Document("PDF")

    input >> decision >> db
    decision >> doc