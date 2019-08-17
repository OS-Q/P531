from platformio.managers.platform import PlatformBase


class Espressif8266Platform(PlatformBase):

    def configure_default_packages(self, variables, targets):
        framework = variables.get("pioframework")
        if "buildfs" in targets:
            self.packages['tool-mkspiffs']['optional'] = False
        return PlatformBase.configure_default_packages(
            self, variables, targets)

    def get_boards(self, id_=None):
        result = PlatformBase.get_boards(self, id_)
        if not result:
            return result
        if id_:
            return self._add_upload_protocols(result)
        else:
            for key, value in result.items():
                result[key] = self._add_upload_protocols(result[key])
        return result

    def _add_upload_protocols(self, board):
        if not board.get("upload.protocols", []):
            board.manifest['upload']['protocols'] = ["esptool", "espota"]
        if not board.get("upload.protocol", ""):
            board.manifest['upload']['protocol'] = "esptool"
        return board
