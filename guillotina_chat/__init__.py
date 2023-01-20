from guillotina import configure

app_settings = {
    # provide custom application settings here...
}

configure.role("guillotina_chat.ConversationParticipant",
               "Conversation Participant",
               "Users that are part of a conversation", False)
configure.grant(
    permission="guillotina.ViewContent",
    role="guillotina_chat.ConversationParticipant")
configure.grant(
    permission="guillotina.AccessContent",
    role="guillotina_chat.ConversationParticipant")
configure.grant(
    permission="guillotina.AddContent",
    role="guillotina_chat.ConversationParticipant")


def includeme(root):
    """
    custom application initialization here
    """
    configure.scan('guillotina_chat.api')
    configure.scan('guillotina_chat.install')
    configure.scan('guillotina_chat.content')
    configure.scan('guillotina_chat.subscribers')
    configure.scan('guillotina_chat.serialize')
    configure.scan('guillotina_chat.services')
