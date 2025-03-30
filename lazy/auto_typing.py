from lazy.no_typo import NoTypo


class CodeGenerator:
    typing_genni = None
    link=''
    def play(self):
        self.typing_genni.key_pressed = 'play'

    def pause(self):
        self.typing_genni.key_pressed = 'pause'

    def stop(self):
        self.typing_genni.key_pressed = 'stop'
    def set_path(self,path):
        self.link=path


    def start_app(self):
        if self.typing_genni is not None:
            if self.typing_genni.thread_status == 'stop':
                self.typing_genni = NoTypo(self.link)
                self.typing_genni.start()
            else:
                self.typing_genni.thread_status = 'stop'
                self.typing_genni = NoTypo(self.link)
                print(self.typing_genni)
                self.typing_genni.start()
        else:
            print(self.link)
            self.typing_genni = NoTypo(self.link)
            self.typing_genni.start()

