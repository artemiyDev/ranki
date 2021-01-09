from supermemo2.model import SMTwo
from datetime import date, datetime


def calculateNextRepeatDate(answer_quality, easiness, interval, repetitions):
    smtwo = SMTwo()
    smtwo.calc(quality=answer_quality, easiness=easiness, interval=interval, repetitions=repetitions,
               review_date=date.today())
    return {'review_date': smtwo.review_date, 'easiness': smtwo.easiness, 'interval': smtwo.interval,
            'repetitions': smtwo.repetitions}
