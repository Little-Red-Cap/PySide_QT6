from import_modules import *
from ui.ui_page_data_tab import *
from PySide6.QtSql import QSqlTableModel, QSqlQuery, QSqlDatabase


def create_database_and_table():
    print("Creating database and table...")
    # 创建一个SQLite数据库连接
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("database.db")
    if not db.open():
        print("无法打开数据库")
        return False

        # 创建一个新的表
    query = QSqlQuery()
    query.exec_("""  
        CREATE TABLE IF NOT EXISTS vg_table (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            name TEXT NOT NULL,  
            value INTEGER  
        )  
    """)

    if query.lastError().isValid():
        print("创建表时出错:", query.lastError().text())
        return False

        # 插入一些数据
    query.exec_("INSERT INTO vg_table (name, value) VALUES ('Example 1', 42)")
    query.exec_("INSERT INTO vg_table (name, value) VALUES ('Example 2', 84)")

    if query.lastError().isValid():
        print("插入数据时出错:", query.lastError().text())
        return False

    print("数据库和表已成功创建，并插入了数据")
    return True


class PageDataTab(QDialog, Ui_Form):
    def create_database(self, name="database.db"):
        # 创建一个SQLite数据库连接
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(name)
        if not self.db.open():
            print("无法打开数据库")
            return False

    def create_table(self, name="default_table"):
        # 创建一个新的表
        self.query.exec_("""  
            CREATE TABLE IF NOT EXISTS vg_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name TEXT NOT NULL,  
                value INTEGER  
            )  
        """)
        if self.query.lastError().isValid():
            print("创建表时出错:", self.query.lastError().text())
            return False

    def insert_data(self, json_dict):
        # 插入一些数据
        self.query.exec_("INSERT INTO vg_table (name, value) VALUES ('Example 1', 42)")

    def __init__(self, parent=None):
        super(PageDataTab, self).__init__(parent)
        self.setupUi(self)
        self.query = QSqlQuery()
        self.db = None
        self.create_database("database.db")
        self.create_table()
        # # self.insert_data()
        # # 创建模型和视图
        # self.model = QSqlTableModel(self)
        # self.model.setTable("vg_table")
        # self.model.select()
        # self.tableView.setModel(self.model)

        # # 创建模型和视图
        # self.model = DatabaseModel(self)
        # self.tableView.setModel(self.model)
        #
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.model.update_data)
        # self.timer.start(1000)  # 每秒更新一次
        #
        # QTimer.singleShot(1000, create_database_and_table)  # 立即更新一次
