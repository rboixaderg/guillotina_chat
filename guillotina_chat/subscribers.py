from guillotina import configure
from guillotina.interfaces import (IObjectAddedEvent, IObjectModifiedEvent,
                                   IPrincipalRoleManager)
from guillotina.utils import get_authenticated_user_id

from guillotina_chat.content import IConversation


@configure.subscriber(for_=(IConversation, IObjectAddedEvent))
@configure.subscriber(for_=(IConversation, IObjectModifiedEvent))
async def container_changed(conversation, event):
    user_id = get_authenticated_user_id()
    if user_id not in conversation.users:
        conversation.users.append(user_id)

    manager = IPrincipalRoleManager(conversation)
    for user in conversation.users:
        manager.assign_role_to_principal(
            'guillotina_chat.ConversationParticipant', user)
