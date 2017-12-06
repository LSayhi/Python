# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:35:16 2017

@author: BD
"""

#homework for python 6_1~6_11
#6-1
'''
Liujiangfan={'first_name':'jiangfan',
             'last_name':'Liu',
             'age':'22',
             'city':'Beijing'
            }
for key,value in Liujiangfan.items():
    print("Liujiangfan's "+key+' is '+value)
'''
#6-2
'''
lovenumber={'liujiangfan':'6',
            'liujiaqi':'5',
            'liuyu':'2',
            'liubei':'3',
            'guanyu':'7',
           }
for name,number in lovenumber.items():
    print('\t'+name+"'s favorite number is "+number)
'''
#6-3
'''
words={'list':'A series of paraments sorted in order ',
       'if':'assume',
       'title':'name of something',
       'a':'before b',
       'c':'after b'
      }
for name,meaning in words.items():
    print(' '+name+':\n\t'+meaning)
'''
#6-4
'''
words={'list ':'A series of paraments sorted in order ',
       'if   ':'assume',
       'title':'name of something',
       'a    ':'before b',
       'c    ':'after b'
      }
words['while']="return 'true' if expresstion in 'while' is satisified"
words['elif '] ='use after if'
words['else '] ='use after if or elif'
words['for  '] ='use to express loop'
words['#    '] ='use to express notes'
for name,meaning in words.items():
    print(' '+name+':\t'+meaning)
'''
#6-5
'''
riverflow={'changjiang  ':['hubei','jiangxi','zhejiang',],
           'huanghe     ':['ganshu','henan','shanghai'],
           'heilongjiang':['neimenggu','heilongprovince'],
          }
for river,locations in riverflow.items():
    print(river.title()+' runs through: ')
    for location in locations:
        print('\t'+location)
'''
#6-6
'''
favorite_languages={'jen':'python',
                    'sarah':'c',
                    'phil':'java',
                   }
namelist=['jen','liujiangfan','Phil','liuyu']
for name in namelist:
    if name.lower() in favorite_languages.keys():
        print('You have taken part in this survey,thanks!')
    else:
        print('please start this survey,thank you.')
'''
#6-7
'''
Liujiangfan={'first_name':'jiangfan',
             'last_name':'Liu',
             'age':'22',
             'city':'Beijing'
            }
Liuyu={'first_name':'yu',
             'last_name':'Liu',
             'age':'22',
             'city':'Shangrao'
      }
Liujiaqi={'first_name':'jiaqi',
             'last_name':'Liu',
             'age':'20',
             'city':'Nanchang'
         }
people=[Liujiangfan,Liuyu,Liujiaqi]
for person in people:
    for key,value in person.items():
        print(person['last_name']+person['first_name']+"'s "+
              key+' is '+ value)
    print('\n')
'''
#6-8
'''
cat={'type':'burudongwu',
     'owner_name':'Liujiangfan',
    }
pstitaciforme={'type':'birds',
             'owner_name':'Liuyu'
      }
pets=[cat,pstitaciforme]
for pet in pets:
    for key,value in pet.items():
        print(
              key+' is '+ value)
    print('\n')
'''
#6-9，重复，略
#6-10重复，略
#6-11
'''
cities={
        'Beijing ':{'country':'China',
                    'population':'21.70 million',
                    'fact':'capital of China'
                   },
        'Shanghai':{'country':'China',
                    'population':'23.61 million',
                    'fact':'financial center of China'
                   },
        'tokyo   ':{'country':'Japan',
                    'population':'42.00 million',
                    'fact':'capital of Japan'
                   }
       }
#city stores the city's name,information stores the very city's information
for city,information in cities.items():
    print(city+' belongs to '+information['country']+', '+
          'the population is '+information['population']+
          ', the '+information['fact']+'.'
         )
'''
