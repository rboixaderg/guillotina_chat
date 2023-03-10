from guillotina import configure
from guillotina.interfaces import IResourceSerializeToJsonSummary
from guillotina.json.serialize_content import DefaultJSONSummarySerializer
from guillotina.utils import get_owners
from zope.interface import Interface

from guillotina_chat.content import IConversation, IMessage


@configure.adapter(
    for_=(IConversation, Interface),
    provides=IResourceSerializeToJsonSummary)
class ConversationJSONSummarySerializer(DefaultJSONSummarySerializer):
    async def __call__(self):
        data = await super().__call__()
        data.update({
            'creation_date': self.context.creation_date,
            'title': self.context.title,
            'users': self.context.users
        })
        return data


@configure.adapter(
    for_=(IMessage, Interface),
    provides=IResourceSerializeToJsonSummary)
class MessageJSONSummarySerializer(DefaultJSONSummarySerializer):
    async def __call__(self):

        data = await super().__call__()
        data.update({
            'creation_date': self.context.creation_date,
            'text': self.context.text,
            'author': get_owners(self.context)[0]
        })
        return data
