class DrugAnalyzer:
    def __init__(self, data=[]):
        self.data = data

    def __add__(self, other):
        if len(self.data[0]) != len(other):
            raise ValueError('Improper length of the added list.')

        if type(other[0]) is not str or type(other[1]) is not float or type(other[2]) is not float or type(other[3]) is not float:
            raise ValueError('Wrong type.')

        total_data = self.data
        total_data.append(other)
        return DrugAnalyzer(total_data)

    def verify_series(
        self,
        series_id: str,
        act_subst_wgt: float,
        act_subst_rate: float,
        allowed_imp: float,
    ) -> bool:
    
        lists = list(filter(lambda k: series_id in k[0], self.data))
        pills_weight = sum([liste[1] for liste in lists])
        actives_substances = sum([liste[2] for liste in lists])
        impurities = sum([liste[3] for liste in lists])

        if (len(lists) * act_subst_wgt * (1 + act_subst_rate)) > actives_substances > (len(lists) * act_subst_wgt * (1 - act_subst_rate)):
            if impurities < (allowed_imp * pills_weight):
                return True
        return False
