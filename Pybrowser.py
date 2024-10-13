from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Python Web Browser')

        # Create a layout
        self.layout = QVBoxLayout()

        # Create the browser widget
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))  # Default page

        # Create the URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Add navigation buttons
        self.go_button = QPushButton('Go')
        self.go_button.clicked.connect(self.navigate_to_url)

        self.back_button = QPushButton('kaka')
        self.back_button.clicked.connect(self.browser.back)

        self.forward_button = QPushButton('Forward')
        self.forward_button.clicked.connect(self.browser.forward)

        self.reload_button = QPushButton('Reload')
        self.reload_button.clicked.connect(self.browser.reload)

        # Set up the layout
        self.container = QWidget()
        self.layout.addWidget(self.url_bar)
        self.layout.addWidget(self.go_button)
        self.layout.addWidget(self.back_button)
        self.layout.addWidget(self.forward_button)
        self.layout.addWidget(self.reload_button)
        self.layout.addWidget(self.browser)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

if __name__ == '__main__':
    app = QApplication([])
    window = Browser()
    window.show()
    app.exec_()
