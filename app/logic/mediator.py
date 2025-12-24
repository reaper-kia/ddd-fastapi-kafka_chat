from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from app.domain.eventes.base import BaseEvent
from app.logic.commands.base import CR, CT, BaseCommand, CommandHandler
from app.logic.events.base import ER, ET, EventHandler
from app.logic.exception.mediator import (
    CommandHandlersNotRegisteredException,
    EventHandlersNotRegisteredException,
)

@dataclass(eq=False)
class Mediator:
    events_map: dict[ET, list[EventHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )
    commands_map: dict[CT, list[CommandHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def register_event(
        self,
        event: ET,
        event_handlers: Iterable[EventHandler[ET, ER]],
    ):
        self.events_map[event].extend(event_handlers)

    def register_command(
        self,
        command: CT,
        command_handlers: Iterable[CommandHandler[CT, CR]],
    ):
        self.commands_map[command].extend(command_handlers)

    async def handler_event(self, event: BaseEvent) -> Iterable[ER]:
        event_type = event.__class__
        handlers = self.events_map.get(event_type)

        if not handlers:
            raise EventHandlersNotRegisteredException(event_type)

        return [await handler.handle(event) for handler in handlers]

    async def handler_commands(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)

        if not handlers:
            raise CommandHandlersNotRegisteredException(command_type)

        return [await handler.handler(command) for handler in handlers]
