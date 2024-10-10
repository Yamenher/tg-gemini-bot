from .config import ALLOWED_USERS, ADMIN_ID, AUCH_ENABLE, ALLOWED_GROUPS



def is_authorized(is_group, from_id: int, user_name: str, chat_id, group_name) -> bool:
    if 0==0 :
        return True


def is_admin(from_id: int) -> bool:
    if str(from_id) == ADMIN_ID:
        return True
    return False
