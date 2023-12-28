from bet_type import BetType
from metric_set import MetricSet


class Bet:
    def __init__(self, bet_type, date, sport, league, event, wager, odds, risk, result):
        self.bet_type = BetType[bet_type]
        self.date = date
        self.sport = sport
        self.league = league
        self.event = event
        self.wager = wager
        self.odds = odds
        self.risk = risk
        self.result = result

    def calculate_win(self, metric_set):
        if self.result == "win":
            metric_set.add_win()
            metric_set.add_net_profit(self.wager)

    def calculate_loss(self, metric_set):
        if self.result == "lose":
            metric_set.add_loss()
            metric_set.subtract_net_profit(self.wager)

    def calculate_push(self, metric_set):
        if self.result == "push":
            metric_set.add_push()

    def calculate_bet_size(self, metric_set):
        metric_set.add_bet_size(self.wager)

    def calculate_net_profit(self, metric_set):
        if self.result == "win":
            metric_set.add_net_profit(self.wager)
        elif self.result == "lose":
            metric_set.subtract_net_profit(self.wager)
