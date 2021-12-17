from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import os
class Downloader:

    def __init__(self) -> None:
        qfiles = QFile('../ui/PackageManager.ui')
        qfiles.open(QFile.ReadOnly)
        qfiles.close()
        self.ui = QUiLoader().load(qfiles)

        self.ui.DownloadButton.clicked.connect(self.download)
        self.ui.actionAuthor.triggered.connect(self.showAuthor)
        self.ui.libcheck.clicked.connect(self.package_check)
    def showAuthor(self):
        QMessageBox.about(self.ui,"作者介绍","简易Python库管理工具\nBy:Elin\n@2021 revision0.01")
    def download(self):
        self.ui.std_output.append('请等待....')
        package_name = self.ui.PackageNameInput.toPlainText()
        Mirror = self.ui.MirrorChooser.currentText()
        MirrorLink = None
        if Mirror == "清华大学":
            MirrorLink = "http://pypi.tuna.tsinghua.edu.cn/simple"
        elif Mirror == "阿里云":
            MirrorLink = "https://mirrors.aliyun.com/pypi/simple/"
        elif Mirror == "网易":
            MirrorLink = "https://mirrors.163.com/pypi/simple/"
        elif Mirror == "腾讯":
            MirrorLink = "https://mirrors.cloud.tencent.com/pypi/simple"
        elif Mirror == "东软":
            MirrorLink = "https://mirrors.neusoft.edu.cn/pypi/web/simple"
        elif MirrorLink == "华为":
            MirrorLink = "https://mirrors.huaweicloud.com/repository/pypi/simple"
        try:
            run_result = os.popen(f"pip install {package_name} -i {MirrorLink}")
            for i in run_result:
                self.ui.std_output.append(str(i))
        except Exception as Error:
            self.ui.std_output.append(str(Error))
    def package_check(self):
        packages = os.popen("pip list").readlines()
        for i in packages:
            self.ui.std_output_2.append(i)
app = QApplication([])
downloader = Downloader()
downloader.ui.show()
app.exec()