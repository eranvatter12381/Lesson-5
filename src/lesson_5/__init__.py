import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lesson 5")
        self.setMinimumWidth(200)
        self.resize(300, 180)

        central_widget = QWidget()
        layout = QHBoxLayout(central_widget)
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        self.counter = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)

        self.value_spinbox = QSpinBox()
        self.value_spinbox.setRange(0, 10_000)
        self.value_spinbox.setPrefix("Value: ")
        self.value_spinbox.setReadOnly(True)
        self.value_spinbox.setStyleSheet("""
            QSpinBox {
                background-color: #e5e5e5;
                border: 1px solid #a0a0a0;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                width: 0;
                height: 0;
            }
        """)

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self._toggle_state)

        self.status_label = QLabel("Stopped")

        left_layout.addWidget(QLabel("Select a value"))
        left_layout.addWidget(self.value_spinbox)
        left_layout.addWidget(self.toggle_button)
        left_layout.addWidget(self.status_label)

        self.vertical_slider = QSlider(Qt.Orientation.Vertical)
        self.vertical_slider.setRange(0, 10_000)

        self.slider_spinbox = QSpinBox()
        self.slider_spinbox.setRange(0, 10_000)
        self.slider_spinbox.setReadOnly(True)
        self.vertical_slider.valueChanged.connect(self.slider_spinbox.setValue)

        right_layout.addWidget(self.vertical_slider)
        right_layout.addWidget(self.slider_spinbox)

        layout.addLayout(left_layout)
        layout.addLayout(right_layout)

        self.setCentralWidget(central_widget)

    def _toggle_state(self, running: bool) -> None:
        self.toggle_button.setText("Stop" if running else "Start")
        self.status_label.setText("Running" if running else "Stopped")
        if running:
            self.timer.start(100)
        else:
            self.timer.stop()

    def timer_method(self) -> None:
        if self.counter >= 10_000:
            self.toggle_button.setChecked(False)
            return

        self.counter += 1
        self.value_spinbox.setValue(self.counter)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
