import argparse
from datetime import datetime
from decimal import Decimal

_2019_MAX_AMOUNT = Decimal(19000)
_COMPANY_MATCH_PERCENT = Decimal('.04')
_QUANTIZE = Decimal('.01')


def parse_args():
    parser = argparse.ArgumentParser(
        description='Calculate how much to contribute.'
    )
    parser.add_argument(
        '--cont',
        action='append',
        type=Decimal,
        help='What amount have you contributed already this year?'
    )
    parser.add_argument(
        'salary',
        metavar='N',
        type=Decimal,
        help='What is your current yearly salary?'
    )

    args = parser.parse_args()
    return args


def remaining_pay_periods():
    # twice a month on the 15th and 30th
    _now = datetime.now()
    remaining_months = 12 - _now.month
    current_day = _now.day
    if current_day < 14:
        remaining_periods_this_month = 2
    elif current_day < 29:
        remaining_periods_this_month = 1
    else:
        remaining_periods_this_month = 0

    return (2 * remaining_months) + remaining_periods_this_month


def run():
    args = parse_args()
    paychecks = remaining_pay_periods()
    ytd_contributions = sum(args.cont)
    remaining_amount = _2019_MAX_AMOUNT - ytd_contributions
    your_salary = Decimal(args.salary)
    salary_per_period = your_salary / Decimal(12 * 2.)
    minimum_contribution = salary_per_period * _COMPANY_MATCH_PERCENT
    combined_min_contribution = Decimal(paychecks * minimum_contribution)

    print(
        'You earn {} per pay period.'.format(
            Decimal(salary_per_period.quantize(_QUANTIZE))
        )
    )
    print(
        'You have already contributed {} this year '
        '({} left of {} max).'.format(
            ytd_contributions,
            remaining_amount,
            _2019_MAX_AMOUNT,
        )
    )
    print(
        'Your minimum contribition should be {} to maximize the '
        '{} company match.'.format(
            Decimal(minimum_contribution.quantize(_QUANTIZE)),
            '{0:.0%}'.format(_COMPANY_MATCH_PERCENT),
        )
    )
    print(
        'There are {} pay periods remaining. '
        'If you contribute the minimum (plus past contributions), '
        'your total will be {}.'
        .format(
            paychecks,
            (ytd_contributions + combined_min_contribution).quantize(
                _QUANTIZE
            ),
        )
    )

    max_contribution_per_paycheck = Decimal(remaining_amount / paychecks)
    max_percent_per_paycheck = Decimal(
        max_contribution_per_paycheck / salary_per_period
    )
    print(
        'To maximize your 401k, you should contribute {} '
        'each remaining pay-period '
        '(or {}).'.format(
            max_contribution_per_paycheck.quantize(_QUANTIZE),
            '{0:.0%}'.format(max_percent_per_paycheck),
            # max_percent_per_paycheck.quantize(_QUANTIZE)
        )
    )

if __name__ == '__main__':
    run()
