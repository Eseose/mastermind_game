from sqlalchemy import select
from app_config import APP_CONFIG
from model import GameModel


class LeaderBoard:

    @staticmethod
    def get_leaders(difficulty=None, limit=3):
        if difficulty is None:
            difficulty = APP_CONFIG.difficulty

        session = APP_CONFIG.get_db_session()
        results = []
        stmt = select(GameModel).where((GameModel.won == True) & (GameModel.difficulty == difficulty)).order_by(
            GameModel.time_elapsed).limit(limit)
        for game_model in session.scalars(stmt):
            results.append(game_model)
        return results
