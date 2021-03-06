from wechaty import FileBox, get_logger
from .contact import Contact
from typing import Optional
import asyncio

log = get_logger('contact_self')


class ContactSelf(Contact):

    async def avatar(self, file: Optional[FileBox] = None) -> FileBox:
        """

        :param file:
        :return:
        """
        log.info('Contact', 'avatar(%s)' % file.name if file else '')
        if not file:
            file_box = await super().avatar(None)
            return file_box

        if self.contact_id != self.puppet.self_id():
            raise Exception('set avatar only available for user self')

        await self.puppet.contact_avatar(self.contact_id, file)

    async def qr_code(self) -> str:
        """

        :return:
        """
        puppet_id: str
        try:
            puppet_id = self.puppet.self_id()
        except Exception as e:
            raise Exception('Can not get qr_code, user might be either not logged in or already logged out')

        if self.contact_id != puppet_id:
            raise Exception('only can get qr_code for the login user self')
        qr_code_value = await self.puppet.contact_self_qr_code()
        return qr_code_value

    @property
    def name(self):
        """

        :return:
        """

    @name.setter
    def name(self, name: Optional[str]) -> str:
        puppet_id: str
        try:
            puppet_id = self.puppet.self_id()
        except Exception as e:
            raise Exception('Can not get qr_code, user might be either not logged in or already logged out')

        if self.contact_id != puppet_id:
            raise Exception('only can get qr_code for the login user self')

        return asyncio.run(self.puppet.contact_self_name(name))

    async def signature(self, signature: str):
        """

        :param signature:
        :return:
        """
        puppet_id: str
        try:
            puppet_id = self.puppet.self_id()
        except Exception as e:
            raise Exception('Can not get qr_code, user might be either not logged in or already logged out')

        if self.contact_id != puppet_id:
            raise Exception('only can get qr_code for the login user self')

        return self.puppet.contact_signature(signature)
