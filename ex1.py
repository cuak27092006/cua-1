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
        self.point_diff = self.points_scored - self.points_allowed

        total_games = self.wins + self.losses
        if total_games > 0:
            self.win_rate = self.wins / total_games
        else:
            self.win_rate = 0

    def evaluate_rank(self):
        if self.win_rate >= 0.8:
            self.rank_status = "Ứng viên vô địch"
        elif self.win_rate >= 0.5:
            self.rank_status = "Playoff"
        else:
            self.rank_status = "Yếu"


class LeagueManager:
    def __init__(self):
        self.teams = []

    def find_code(self, code):
        for team in self.teams:
            if team.code == code:
                return team
        return None

    def add_team(self):
        while True:
            code = input("Nhập mã đội: ")

            if not code:
                print("Mã đội không được để trống!")
                continue

            if self.find_code(code):
                print("Mã đội đã tồn tại!")
                continue

            break

        team_name = input("Nhập tên đội: ")

        wins = int(input("Số trận thắng: "))
        losses = int(input("Số trận thua: "))
        points_scored = int(input("Tổng điểm ghi được: "))
        points_allowed = int(input("Tổng điểm bị ghi: "))

        team = BasketballTeam(
            code,
            team_name,
            wins,
            losses,
            points_scored,
            points_allowed
        )

        self.teams.append(team)
        print("Thêm đội thành công!")

    def show_ranking(self):
        if not self.teams:
            print("Bảng xếp hạng đang trống!")
            return

        ranking = sorted(
            self.teams,
            key=lambda x: (x.win_rate, x.point_diff),
            reverse=True
        )

        print("\n===== BẢNG XẾP HẠNG =====")

        for i, team in enumerate(ranking, start=1):
            print(
                i,
                team.code,
                team.team_name,
                team.wins,
                team.losses,
                team.point_diff,
                round(team.win_rate * 100, 2),
                "%",
                team.rank_status
            )

    def update_team(self):
        code = input("Nhập mã đội cần cập nhật: ")

        team = self.find_code(code)

        if not team:
            print("Không tìm thấy đội!")
            return

        team.team_name = input("Tên đội mới: ")
        team.wins = int(input("Số trận thắng mới: "))
        team.losses = int(input("Số trận thua mới: "))
        team.points_scored = int(input("Tổng điểm ghi mới: "))
        team.points_allowed = int(input("Tổng điểm bị ghi mới: "))

        team.calculate_stats()
        team.evaluate_rank()

        print("Cập nhật thành công!")

    def delete_team(self):
        code = input("Nhập mã đội cần xóa: ")

        team = self.find_code(code)

        if not team:
            print("Không tìm thấy đội!")
            return

        self.teams.remove(team)
        print("Xóa thành công!")

    def search_team(self):
        keyword = input("Nhập mã hoặc tên đội: ").lower()

        found = False

        for team in self.teams:
            if keyword in team.code.lower() or keyword in team.team_name.lower():
                print(
                    team.code,
                    team.team_name,
                    team.wins,
                    team.losses,
                    team.point_diff,
                    round(team.win_rate * 100, 2),
                    "%",
                    team.rank_status
                )
                found = True

        if not found:
            print("Không tìm thấy đội!")


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
    manager = LeagueManager()

    while True:
        show_menu()

        choice = input("Mời bạn nhập lựa chọn: ")

        match choice:
            case "1":
                manager.show_ranking()

            case "2":
                manager.add_team()

            case "3":
                manager.update_team()

            case "4":
                manager.delete_team()

            case "5":
                manager.search_team()

            case "6":
                print("Thoát chương trình")
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()
