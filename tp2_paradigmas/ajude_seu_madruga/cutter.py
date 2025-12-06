ROUND_DECIMALS = 4
ROUND_DECIMALS_OUTPUT = 4


class PaperCutter:
    def __init__(self, num_papers: int, width_list: list, target_area: int) -> None:
        self.num_papers = num_papers
        self.papers_width_list = width_list
        self.target_area = target_area

    def find_height(self):
        total_sum = sum(self.papers_width_list)
        if self.target_area == 0:
            return "0.0000"
        elif total_sum < self.target_area:
            return "-.-"
        elif self.target_area == total_sum:
            return ":D"
        else:
            min_height = 0
            max_height = max(self.papers_width_list)
            mid_height = (max_height + min_height) / 2
            mid_height_area = 0

            for i in range(60):
                mid_height_area = 0
                for item in self.papers_width_list:
                    if item > mid_height:
                        mid_height_area += item - mid_height
                mid_height_area = round(mid_height_area, ROUND_DECIMALS)

                if mid_height_area < self.target_area:
                    max_height = mid_height
                else:
                    min_height = mid_height

                mid_height = (max_height + min_height) / 2

            return f"{round(mid_height, ROUND_DECIMALS_OUTPUT):.4f}"
