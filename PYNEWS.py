import sys, re, requests, webbrowser, urllib.request
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QGridLayout, QWidget
from PyQt5.Qt import QLabel, QPushButton, QSize, QPixmap
from bs4 import BeautifulSoup
from urllib.request import urlopen


class MainWindow(QMainWindow):
    """Main News window/Front page"""
    def __init__(self):
        super().__init__()
        self.widgets()

    def email(self):
        """Opens default email client and send email to contact"""
        webbrowser.open("mailto: gorm90@gmail.com")

    def on_click_strange(self):
        self.strange = Strange()
        self.strange.show()

    def on_click_economy(self):
        self.eeaw = Economy()
        self.eeaw.show()

    def on_click_tech(self):
        self.feaw = Technology()
        self.feaw.show()

    def on_click_enter(self):
        self.teaw = Entertainment()
        self.teaw.show()

    def widgets(self):
        """Main function, places the widgets etc in the window, also controls window size"""
        self.setWindowTitle("PyNews Latest News")
        self.setMinimumSize(QSize(900, 670))
        self.setMaximumSize(QSize(900, 670))
        self.add_menus_and_status()
        self.create_tool_bar()
        url = "http://feeds.skynews.com/feeds/rss/world.xml"
        self.news_display(url)

    def add_menus_and_status(self):
        """Creating The menu and status bar"""
        self.statusBar().showMessage("")
        menubar = self.menuBar()
        menu = menubar.addMenu("Menu")
        contact_action = QAction("Contact", self)
        contact_action.setStatusTip("Contact PyCrypt")
        contact_action.triggered.connect(self.email)
        menu.addAction(contact_action)
        menu.addSeparator()
        exit_action = QAction("Exit", self)
        exit_action.setStatusTip("Press to Exit The Application")
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut("Ctrl+Q")
        menu.addAction(exit_action)

    def create_tool_bar(self):
        """Creates the toolbar, and displays Qpushbutons within"""
        strange_button = QPushButton("Strange News")
        strange_button.setStatusTip("Click to get the latest in strange news")
        strange_button.clicked.connect(self.on_click_strange)
        economy_button = QPushButton("Economy")
        economy_button.setStatusTip("Click to get the latest economy news")
        economy_button.clicked.connect(self.on_click_economy)
        fashion_button = QPushButton("Technology")
        fashion_button.setStatusTip("Click to get the latest technology news")
        fashion_button.clicked.connect(self.on_click_tech)
        entertainment_button = QPushButton("Entertainment")
        entertainment_button.setStatusTip("Click to get the latest in entertainment")
        entertainment_button.clicked.connect(self.on_click_enter)
        toolbar = self.addToolBar("")
        toolbar.addWidget(strange_button)
        toolbar.addWidget(economy_button)
        toolbar.addWidget(fashion_button)
        toolbar.addWidget(entertainment_button)

    def news_display(self, url):
        """Scraping the given url (url) for news, and sorting them, Asingning link to lbl, placing lbls within
        MainWindow"""
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, features="xml")
        items = soup.findAll('item')
        news_items = []
        for item in items:
            news_item = dict()
            news_item['description'] = item.description.text
            news_item["purelink"] = item.link.text
            news_item['linkat'] = "<a href=\"" + item.link.text + "\">" + item.title.text + "</a>"
            news_items.append(news_item)

        def image_finder(link):
                imagelist = []
                html = urlopen(link)
                bs = BeautifulSoup(html, 'html.parser')
                images = bs.find_all('img', {'src': re.compile('.jpg')})
                for image in images:
                    imagelist.append((image['src']))
                try:
                    return imagelist[0]
                except IndexError:
                    imagelist.append("https://loremflickr.com/320/240")
                    return imagelist[0]

        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(image_finder(news_items[0]["purelink"])).read())
        lbl_1_img = QLabel()
        lbl_1_img.setPixmap(pixmap)

        lbl_1 = QLabel(news_items[0]["linkat"] + "\t" + news_items[0]["description"])
        lbl_1.setOpenExternalLinks(True), lbl_1.setWordWrap(True), lbl_1.setStatusTip(news_items[0]["purelink"])

        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(image_finder(news_items[1]["purelink"])).read())
        lbl_2_img = QLabel()
        lbl_2_img.setPixmap(pixmap)

        lbl_2 = QLabel(news_items[1]["linkat"] + "\t" + news_items[1]["description"])
        lbl_2.setOpenExternalLinks(True), lbl_2.setWordWrap(True), lbl_2.setStatusTip(news_items[1]["purelink"])

        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(image_finder(news_items[2]["purelink"])).read())
        lbl_3_img = QLabel()
        lbl_3_img.setPixmap(pixmap)

        lbl_3 = QLabel(news_items[2]["linkat"] + "\t" + news_items[2]["description"])
        lbl_3.setOpenExternalLinks(True), lbl_3.setWordWrap(True), lbl_3.setStatusTip(news_items[2]["purelink"])

        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(image_finder(news_items[3]["purelink"])).read())
        lbl_4_img = QLabel()
        lbl_4_img.setPixmap(pixmap)

        lbl_4 = QLabel(news_items[3]["linkat"] + "\t" + news_items[3]["description"])
        lbl_4.setOpenExternalLinks(True), lbl_4.setWordWrap(True), lbl_4.setStatusTip(news_items[3]["purelink"])

        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(image_finder(news_items[4]["purelink"])).read())
        lbl_5_img = QLabel()
        lbl_5_img.setPixmap(pixmap)

        lbl_5 = QLabel(news_items[4]["linkat"] + "\t" + news_items[4]["description"])
        lbl_5.setOpenExternalLinks(True), lbl_5.setWordWrap(True), lbl_5.setStatusTip(news_items[4]["purelink"])

        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(image_finder(news_items[5]["purelink"])).read())
        lbl_6_img = QLabel()
        lbl_6_img.setPixmap(pixmap)

        lbl_6 = QLabel(news_items[5]["linkat"] + "\t" + news_items[5]["description"])
        lbl_6.setOpenExternalLinks(True), lbl_6.setWordWrap(True), lbl_6.setStatusTip(news_items[5]["purelink"])

        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(image_finder(news_items[6]["purelink"])).read())
        lbl_7_img = QLabel()
        lbl_7_img.setPixmap(pixmap)

        lbl_7 = QLabel(news_items[6]["linkat"] + "\t" + news_items[6]["description"])
        lbl_7.setOpenExternalLinks(True), lbl_7.setWordWrap(True), lbl_7.setStatusTip(news_items[6]["purelink"])

        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(image_finder(news_items[7]["purelink"])).read())
        lbl_8_img = QLabel()
        lbl_8_img.setPixmap(pixmap)

        lbl_8 = QLabel(news_items[7]["linkat"] + "\t" + news_items[7]["description"])
        lbl_8.setOpenExternalLinks(True), lbl_8.setWordWrap(True), lbl_8.setStatusTip(news_items[7]["purelink"])

        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(image_finder(news_items[8]["purelink"])).read())
        lbl_9_img = QLabel()
        lbl_9_img.setPixmap(pixmap)

        lbl_9 = QLabel(news_items[8]["linkat"] + "\t" + news_items[8]["description"])
        lbl_9.setOpenExternalLinks(True), lbl_9.setWordWrap(True), lbl_9.setStatusTip(news_items[8]["purelink"])

        g_layout = QGridLayout()

        g_layout.addWidget(lbl_1_img, 0, 0), g_layout.addWidget(lbl_2_img, 0, 1), g_layout.addWidget(lbl_3_img, 0, 2)
        g_layout.addWidget(lbl_1, 1, 0), g_layout.addWidget(lbl_2, 1, 1), g_layout.addWidget(lbl_3, 1, 2)
        g_layout.addWidget(lbl_4_img, 2, 0), g_layout.addWidget(lbl_5_img, 2, 1), g_layout.addWidget(lbl_6_img, 2, 2)
        g_layout.addWidget(lbl_4, 3, 0), g_layout.addWidget(lbl_5, 3, 1), g_layout.addWidget(lbl_6, 3, 2)
        g_layout.addWidget(lbl_7_img, 4, 0), g_layout.addWidget(lbl_8_img, 4, 1), g_layout.addWidget(lbl_9_img, 4, 2)
        g_layout.addWidget(lbl_7, 5, 0), g_layout.addWidget(lbl_8, 5, 1), g_layout.addWidget(lbl_9, 5, 2)

        layout_widget = QWidget()
        layout_widget.setLayout(g_layout)
        self.setCentralWidget(layout_widget)


class Strange(MainWindow):
    def widgets(self):
        """Main function, places the widgets etc in the window, also controls window size"""
        self.setWindowTitle("PyNews Strange ")
        self.setMinimumSize(QSize(900, 670))
        self.setMaximumSize(QSize(900, 670))
        self.add_menus_and_status()
        self.create_tool_bar()
        url = "http://feeds.skynews.com/feeds/rss/strange.xml"
        self.news_display(url)


class Entertainment(MainWindow):
    def widgets(self):
        """Main function, places the widgets etc in the window, also controls window size"""
        self.setWindowTitle("PyNews entertainment")
        self.setMinimumSize(QSize(900, 670))
        self.setMaximumSize(QSize(900, 670))
        self.add_menus_and_status()
        self.create_tool_bar()
        url = "http://feeds.skynews.com/feeds/rss/entertainment.xml"
        self.news_display(url)


class Economy(MainWindow):
    def widgets(self):
        """Main function, places the widgets etc in the window, also controls window size"""
        self.setWindowTitle("PyNews Economy")
        self.setMinimumSize(QSize(900, 670))
        self.setMaximumSize(QSize(900, 670))
        self.add_menus_and_status()
        self.create_tool_bar()
        url = "http://feeds.skynews.com/feeds/rss/business.xml"
        self.news_display(url)


class Technology(MainWindow):
    def widgets(self):
        """Main function, places the widgets etc in the window, also controls window size"""
        self.setWindowTitle("PyNews Tech")
        self.setMinimumSize(QSize(900, 670))
        self.setMaximumSize(QSize(900, 670))
        self.add_menus_and_status()
        self.create_tool_bar()
        url = "http://feeds.skynews.com/feeds/rss/technology.xml"
        self.news_display(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())
