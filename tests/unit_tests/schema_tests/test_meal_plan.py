from datetime import datetime

import pytest

from mealie.schema.meal_plan.plan_rules import PlanRulesDay

test_cases = [
    (datetime(2022, 2, 7, tzinfo=datetime.UTC), PlanRulesDay.monday),
    (datetime(2022, 2, 8, tzinfo=datetime.UTC), PlanRulesDay.tuesday),
    (datetime(2022, 2, 9, tzinfo=datetime.UTC), PlanRulesDay.wednesday),
    (datetime(2022, 2, 10, tzinfo=datetime.UTC), PlanRulesDay.thursday),
    (datetime(2022, 2, 11, tzinfo=datetime.UTC), PlanRulesDay.friday),
    (datetime(2022, 2, 12, tzinfo=datetime.UTC), PlanRulesDay.saturday),
    (datetime(2022, 2, 13, tzinfo=datetime.UTC), PlanRulesDay.sunday),
]


@pytest.mark.parametrize("date, expected", test_cases)
def test_date_obj_to_enum(date: datetime, expected: PlanRulesDay):
    assert PlanRulesDay.from_date(date) == expected
