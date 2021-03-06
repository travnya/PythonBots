from LeagueBot import menu
import pytest

# Тест отправляемых ботом сообщений в функции "menu"
@pytest.mark.parametrize("Message", [('Выберите интересующий Вас раздел'),(         '''
  000000   00000
 00000000 0000000
 0000000000000000
  00000000000000
    00000000000
       00000
         0
        *  000000   00000
       *  00000000 0000000
      *   0000000000000000
      *    00000000000000
       *     00000000000
        *       00000
         *        0
 000000   00000   *
00000000 0000000   *
0000000000000000    *
 00000000000000     *
   00000000000     *
      00000       *
        0        *
        *  000000   00000
       *  00000000 0000000
      *   0000000000000000
      *    00000000000000
      *      00000000000
       *        00000
        *         0
         *        *
                   *
                    *
                     *
                      *
                       *
            ''')
    ,('Все самые востребованные ссылки в Лиге:\n\n',('Академия Лиги\n','https://academy.digitalleague.ru/'),
                             ('FAQ Лиги\n','https://academy.digitalleague.ru/faq'),
                             ('СДО Лиги\n','https://sdo.digitalleague.ru/courses'),
                             ('ИПР Лиги\n','https://academy.digitalleague.ru/idp/'),
                             ('Интранет Лиги','https://intranet.digitalleague.ru/'))
    ,('\n• Разутвердить гайдбук нельзя по причине того, что он может быть выбран (определен) у сотрудников в рамках данной сессии, которые могли начать оценку.')
    ,("Я не понимаю о чем вы говорите")
    ,(1112321),(44/3231),(1.2),(11*16)])
def test_menu(Message):
    assert menu(message=Message)