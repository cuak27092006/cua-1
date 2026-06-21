class BasketballTeam:
    def __init__(self, code, team_name, wins, losses, points_scored, points_allowed):
        self.code = code
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.points_scored = points_scored
        self.points_allowed = points_allowed

        self.point_diff = 0
        self.win_rate = 0
        self.rank_status = ""

        self.calculate_stats()
        self.evaluate_rank()
    def calculate_stats(self):
        point_diff = self.scored - self.allowed
        self.point_diff = point_diff
        win_rate = self.wins / (self.wins + self.losses)
        self.win_rate = win_rate
    def evaluate_rank(self):
        if self.win_rate >= 0.8 :
            self.rank_status = "Ứng viên vô địch"
        elif self.win_rate == 0.5 :
            self.rank_status = "Playoff"
        else :
            self.rank_status = "Yếu"
       

class LeagueManager:
    def __init__(self):
        self.teams = []
    def find_code(self,code):
        pass
    def add_team(self):
        pass
    def show_ranking(self):
        if not self.teams :
            print("bảng xếp hạng đang trống")
            return
        print(f"|{''}|{''}|{''}|{''}|{''}|{''}|{''}|{''}|{''}|")
        for t in self.teams:
              print(f"|{''}|{''}|{''}|{''}|{''}|{''}|{''}|{''}|{''}|")
      

    def update_team(self):
        pass
    def delete_team(self):
        pass
    def search_team(self):
        pass
def show_menu():
    print("""
1. Hiển thị BXH
2. Thêm đội
3. Cập nhật
4. Xóa
5. Tìm kiếm
6. Thoát
""")
def main():
    manager = LeagueManager
    while True:
        show_menu()
        choice = input("mời bạn nhập vào lựa chọn :")
        match choice:
            case "1":
                manager.show_ranking
            case "2":
                manager.add_team
            case "3":
                manager.update_team
            case "4":
                manager.delete_team
            case "5":
                manager.search_team
            case "6":
                print("Thoát trương trình")
                break
            case _:
                print("lựa chọn không hợp lệ")
    



       