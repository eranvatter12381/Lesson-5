import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lesson 5")
        self.setFixedSize(300, 180)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.value_spinbox = QSpinBox()
        self.value_spinbox.setRange(0, 10_000)
        self.value_spinbox.setPrefix("Value: ")

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self._toggle_state)

        self.status_label = QLabel("Stopped")

        layout.addWidget(QLabel("Select a value"))
        layout.addWidget(self.value_spinbox)
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.status_label)

        self.setCentralWidget(central_widget)

    def _toggle_state(self, running: bool) -> None:
        self.toggle_button.setText("Stop" if running else "Start")
        self.status_label.setText("Running" if running else "Stopped")


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
