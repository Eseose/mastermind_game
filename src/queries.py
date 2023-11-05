from sqlalchemy import select
from src.app_config import APP_CONFIG
from src.model import GameModel, RoundModel


class Queries:

    @staticmethod
    def get_leaders(difficulty=None, limit=3):
        if difficulty is None:
            difficulty = APP_CONFIG.difficulty

        session = APP_CONFIG.get_db_session()
        leaders = []
        stmt = select(GameModel).where(
            (GameModel.won == True) & (GameModel.difficulty == difficulty)
        ).order_by(
            GameModel.time_elapsed).limit(limit)
        for game_model in session.scalars(stmt):
            leaders.append(game_model)
        return leaders

    @staticmethod
    def get_rounds():
        session = APP_CONFIG.get_db_session()
        rounds = []
        stmt = select(RoundModel).where(
            (RoundModel.game_id == APP_CONFIG.current_game_id)
        ).order_by(RoundModel.attempt)
        for round_model in session.scalars(stmt):
            rounds.append(round_model)
        return rounds
