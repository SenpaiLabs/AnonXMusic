# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


from pyrogram import filters, types

from anony import app, db, lang
from anony.helpers import admin_check


@app.on_message(filters.command("autoplay") & filters.group & ~app.bl_users)
@lang.language()
@admin_check
async def _autoplay(_, m: types.Message):
    if len(m.command) != 2 or m.command[1].lower() not in {"on", "off"}:
        return await m.reply_text("Usage: /autoplay on or /autoplay off")

    enabled = m.command[1].lower() == "on"
    await db.set_autoplay(m.chat.id, enabled)
    status = "enabled" if enabled else "disabled"
    await m.reply_text(f"Autoplay {status}.")
