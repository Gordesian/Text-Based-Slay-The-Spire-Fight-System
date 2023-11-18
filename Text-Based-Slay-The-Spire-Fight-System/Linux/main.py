import random
import os
hp = 80
gameEnd = False
encounterWon = True
errorS = True
while errorS:
  try:
    print("Enter Encounter Number")
    print("   1 - Normal Start")
    print("  -1 - 1000 HP Enemy Type 3")
    print("  -3 - 1000 HP Enemy Type 4")
    encounterSelect = True
    while encounterSelect:
      encounter = int(input()) #1-5: Normal | -1: 10**3 type 3 | -3: 5*10**3 type 4
      if (((encounter >= 1) and (encounter <= 5)) or (encounter == -1) or (encounter == -3)):
        encounterSelect = False
        errorS = False
        os.system('clear')
  except:
    print("Input a number")
playCards = ['Strike','Strike','Strike','Strike','Strike','Defend','Defend','Defend','Defend','Bash']
def cardDescription(cardList):
  if 'Strike' in cardList:
    print()
    print('Strike')
    print('Deal 6 damage')
    print('Costs 1 energy')
  if 'Defend' in cardList:
    print()
    print('Defend')
    print('Gain 5 block')
    print('Costs 1 energy')
  if 'Bash' in cardList:
    print()
    print('Bash')
    print('Deal 8 damage')
    print('Costs 2 energy')
  if 'Anger' in cardList:
    print()
    print('Anger')
    print('Deal 6 damage')
    print('Add a copy of this card to your discard pile')
    print('Costs 0 energy')
  if 'Cleave' in cardList:
    print()
    print('Cleave')
    print('Deal 8 damage to all enemies')
    print('Costs 1 energy')
  if 'Body Slam' in cardList:
    print()
    print('Body Slam')
    print('Deal damage equal to your current block')
    print('Costs 1 energy')
  if 'Iron Wave' in cardList:
    print()
    print('Iron Wave')
    print('Deal 5 damage')
    print('Gain 5 block')
    print('Costs 1 energy')
  if 'Perfected Strike' in cardList:
    print()
    print('Perfected Strike')
    print('Deal 6 damage')
    print('Deals an additional 2 damage for ALL of your cards containing "Strike"')
    print('Costs 2 energy')
  if 'Bloodletting' in cardList:
    print()
    print('Bloodletting')
    print('Lose 3 Hp')
    print('Gain 2 Energy')
    print('Costs 0 energy')
  if 'Pommel Strike' in cardList:
    print()
    print('Pommel Strike')
    print('Deal 9 damage')
    print('Draw 1 card')
    print('Costs 1 energy')
  if 'Shrug it Off' in cardList:
    print()
    print('Shrug it Off')
    print('Gain 8 block')
    print('Draw 1 card')
    print('Costs 1 energy')
  if 'Entrench' in cardList:
    print()
    print('Entrench')
    print('Double your current block')
    print('Costs 2 energy')
  if 'Rampage' in cardList:
    print()
    print('Rampage')
    print('Deal 8 damage')
    print("Increase this card's damage by 5 this combat")
    print('Costs 1 energy')
  if 'Dazed' in cardList:
    print()
    print('Dazed')
    print('Unplayable')
    print('Ethereal')
  if 'Void' in cardList:
    print()
    print('Void')
    print('Unplayable')
    print('When this card is drawn, lose 1 Energy')
    print('Ethereal')
  if 'Clothesline' in cardList:
    print()
    print('Clothesline')
    print('Deal 12 damage')
    print('Costs 2 energy')
  if 'Sword Boomerang' in cardList:
    print()
    print('Sword Boomerang')
    print('Deal 3 damage to a random enemy 3 times')
    print('Costs 1 energy')
  if 'Thunderclap' in cardList:
    print()
    print('Thunderclap')
    print('Deal 4 damage to all enemies')
    print('Costs 1 energy')
  if 'Twin Strike' in cardList:
    print()
    print('Twin Strike')
    print('Deal 5 damage twice')
    print('Costs 1 energy')
def cardGain():
  cardGainList = ['Anger','Bash','Strike','Defend','Cleave','Body Slam','Iron Wave','Perfected Strike','Bloodletting','Pommel Strike','Shrug it Off','Entrench','Rampage','Clothesline','Sword Boomerang','Thunderclap','Twin Strike']
  cardGainOptions = random.choices(cardGainList,k=3)
  return cardGainOptions
def cardGain2(playCards):
  cardGainOptions = cardGain()
  print('Choose a card: ',cardGainOptions)
  cardDescription(cardGainOptions)
  print()
  error1 = True
  while error1:
    try:
      choiceCard = int(input("Input 1, 2, 3, or 0 to Skip "))
      if not choiceCard==0:
        cardGainChoice = cardGainOptions[choiceCard-1]
        playCards.append(cardGainChoice)
      error1 = False
    except:
      print("Input a number")
  return playCards;
def cardChoice(card,cards,discardPile,exhaustPile):
  error = True
  while error:
    try:
      card = int(input('Choose the card to play (0 to end turn) '))
      correction = True
      while correction:
        if card>len(cards):
          card = int(input('Choose the card to play '))
        else:
          correction = False
    except:
      print("Input a number")
    else:
      if card==0:
        cardID = 0
      else:
        exhaust = False
        if cards[(card-1)]=='Strike':
          cardID = 1
        elif cards[(card-1)]=='Defend':
          cardID = 2
        elif cards[(card-1)]=='Bash':
          cardID = 3
        elif cards[(card-1)]=='Anger':
          cardID = 4
        elif cards[(card-1)]=='Cleave':
          cardID = 5
        elif cards[(card-1)]=='Body Slam':
          cardID = 6
        elif cards[(card-1)]=='Iron Wave':
          cardID = 7
        elif cards[(card-1)]=='Perfected Strike':
          cardID = 8
        elif cards[(card-1)]=='Bloodletting':
          cardID = 9
        elif cards[(card-1)]=='Pommel Strike':
          cardID = 10
        elif cards[(card-1)]=='Shrug it Off':
          cardID = 11
        elif cards[(card-1)]=='Entrench':
          cardID = 12
        elif cards[(card-1)]=='Rampage':
          cardID = 13
        elif cards[(card-1)]=='Dazed':
          cardID = 14
          exhaust = True
        elif cards[(card-1)]=='Void':
          cardID = 14
          exhaust = True
        elif cards[(card-1)]=='Clothesline':
          cardID = 15
        elif cards[(card-1)]=='Sword Boomerang':
          cardID = 16
        elif cards[(card-1)]=='Thunderclap':
          cardID = 17
        elif cards[(card-1)]=='Twin Strike':
          cardID = 18
        if exhaust==True:
          exhaustPile.append(cards[(card-1)])
        else:
          discardPile.append(cards[(card-1)])
        print(cards[(card-1)])
        cards.pop((card-1))
      error = False
      return cardID,cards,discardPile,exhaustPile
def targetTime():
  targeting = True
  while targeting:
    error = True
    while error:
      try:
        target = int(input('Which Enemy? (1-left 2-middle 3-right) '))
        error = False
      except:
        print("Input a number")
    if target==1 or target==2 or target==3:
      targeting = False
  return target
def card(cardID,energy,discardPile,shield,playCards,rampageCounter,playerTurn): #ID 1-Strike ID 2-Defend
  attack = 0
  target = 0
  block = 0
  cost = 0
  hurt = 0
  draw = 0
  allTarget = False
  randomAttack = False
  attackTimes = 1
  if cardID==0:
    playerTurn = False
  elif cardID==1:
    if energy>=1:
      target = targetTime()
      attack = 6
      cost = 1
  elif cardID==2:
    if energy>=1:
      block = 5
      cost = 1
  elif cardID==3:
    if energy>=2:
      target = targetTime()
      attack = 8
      cost = 2
  elif cardID==4:
    target = targetTime()
    attack = 6
    discardPile.append('Anger')
  elif cardID==5:
    if energy>=1:
      allTarget = True
      attack = 8
      cost = 1
  elif cardID==6:
    if energy>=1:
      target = targetTime()
      attack = shield
      cost = 1
  elif cardID==7:
    if energy>=1:
      target = targetTime()
      attack = 5
      block = 5
      cost = 1
  elif cardID==8:
    if energy>=2:
      target = targetTime()
      strikeCount = 0
      for i in playCards:
        if i in 'Strike':
          strikeCount += 1
      attack = 6 + 3*strikeCount
      cost = 2
  elif cardID==9:
    hurt = 3
    cost = -2
  elif cardID==10:
    if energy>=1:
      target = targetTime()
      attack = 9
      draw = 1
      cost = 1
  elif cardID==11:
    if energy>=1:
      block = 8
      draw = 1
      cost = 1
  elif cardID==12:
    if energy>=2:
      block = shield
      cost = 2
  elif cardID==13:
    if energy>=1:
      target = targetTime()
      attack = 8 + 5*rampageCounter
      rampageCounter += 1
      cost = 1
  elif cardID==15:
    if energy>=2:
      target = targetTime()
      attack = 12
      cost = 2
  elif cardID==16:
    if energy>=1:
      attack = 3
      cost = 1
      randomAttack = True
      attackTimes = 3
  elif cardID==17:
    if energy>=1:
      allTarget = True
      attack = 4
      cost = 1
  elif cardID==18:
    if energy>=1:
      target = targetTime()
      attack = 5
      cost = 1
      attackTimes = 2
  return target,attack,block,cost,energy,discardPile,allTarget,hurt,draw,rampageCounter,playerTurn,randomAttack,attackTimes
while hp>0 and (not gameEnd):
  os.system('clear')
  if encounterWon==True:
    enemyBlock = [0,0,0]
    discardPile = []
    exhaustPile = []
    rampageCounter = 0
    if encounter==1:
      enemyType = [1,1,1]
      enemyHp = [15,15,15]
    elif encounter==2:
      playCards = cardGain2(playCards)
      enemyType = [1,2,1]
      enemyHp = [30,30,30]
    elif encounter==3:
      playCards = cardGain2(playCards)
      enemyType = [2,2,2]
      enemyHp = [45,45,45]
    elif encounter==4:
      playCards = cardGain2(playCards)
      enemyType = [2,3,2]
      enemyHp = [60,60,60]
    elif encounter==5:
      playCards = cardGain2(playCards)
      enemyType = [3,3,3]
      enemyHp = [75,75,75]
    elif encounter==-1:
      for i in range(5):
        os.system('clear')
        playCards = cardGain2(playCards)
      enemyType = [3,3,3]
      enemyHp = [10**3,10**3,10**3]
    elif encounter==-3:
      for i in range(25):
        os.system('clear')
        playCards = cardGain2(playCards)
      enemyType = [4,4,4]
      enemyHp = [10**3,10**3,10**3]
    else:
      gameEnd = True
    activeCards = []
    for i in playCards:
      activeCards.append(i)
    encounterWon = False
  if gameEnd==False:
    playerTurn = True
    start = True
    encounterEnd = False
    enemyAction = [0,0,0] #1-attack 5 2-all block 5
    enemyActionRead = []
    for i in range(3):
      enemyChoice = 0
      if enemyType[i]==1:
        enemyChoice = random.randint(1,2)
        if enemyChoice==1:
          enemyActionRead.append('Attack 5')
        if enemyChoice==2:
          enemyActionRead.append('All Block 5')
      elif enemyType[i]==2:
        enemyChoice = random.randint(1,3)
        if enemyChoice==1:
          enemyActionRead.append('Attack 5')
        if enemyChoice==2:
          enemyActionRead.append('All Block 5')
        if enemyChoice==3:
          enemyActionRead.append('3 Dazed Cards')
      elif enemyType[i]==3:
        enemyChoice = random.randint(1,4)
        if enemyChoice==1:
          enemyActionRead.append('Attack 5')
        if enemyChoice==2:
          enemyActionRead.append('All Block 5')
        if enemyChoice==3:
          enemyActionRead.append('3 Dazed Cards')
        if enemyChoice==4:
          enemyActionRead.append('1 Void Card')
      elif enemyType[i]==4:
        enemyChoice = random.randint(4,7)
        if enemyChoice==4:
          enemyActionRead.append('1 Void Card')
        if enemyChoice==5:
          enemyActionRead.append('Attack 1')
        if enemyChoice==6:
          enemyActionRead.append('All Block 10')
        if enemyChoice==7:
          enemyActionRead.append('Attack 100 if they have Block')
      enemyAction[i] += enemyChoice
    while playerTurn and (not encounterEnd):
      os.system('clear')
      print('Enemy Action: ',enemyActionRead)
      print()
      print('Enemy Hp: ',enemyHp)
      print('Enemy Block: ',enemyBlock)
      print()
      if start:
        shield = 0
        energy = 3
        cards = []
        for i in range(7):
          if len(activeCards)==0:
            activeCards = discardPile
            discardPile = []
          activeCard = random.randint(1,len(activeCards))
          cards.append(activeCards[activeCard-1])
          if activeCards[activeCard-1]=='Void':
            energy -= 1
          activeCards.pop(activeCard-1)
        start = False
      print('Card Pile: ',activeCards)
      print('Discard Pile: ',discardPile)
      print('Exhaust Pile: ',exhaustPile)
      cardDescription(cards)
      print()
      print('Health: ',hp)
      print('Energy: ',energy)
      print('Cards: ',cards)
      print('Block: ',shield)
      print()
      cardID,cards,discardPile,exhaustPile = cardChoice(card,cards,discardPile,exhaustPile)
      target,attack,block,cost,energy,discardPile,allTarget,hurt,draw,rampageCounter,playerTurn,randomAttack,attackTimes = card(cardID,energy,discardPile,shield,playCards,rampageCounter,playerTurn)
      shield += block
      hp -= hurt
      if not draw==0:
        for i in range(draw):
          if len(activeCards)==0:
            activeCards = discardPile
            discardPile = []
          activeCard = random.randint(1,len(activeCards))
          cards.append(activeCards[activeCard-1])
          activeCards.pop(activeCard-1)
      if not allTarget and not randomAttack:
        for i in range(attackTimes):
          if enemyBlock[(target-1)]==0:
            enemyHp[(target-1)] -= attack
          else:
            preAttack = attack
            attack -= enemyBlock[(target-1)]
            enemyBlock[(target-1)] -= preAttack
            if enemyBlock[(target-1)]<=0:
              enemyHp[(target-1)] -= attack
            attack = preAttack
      elif allTarget:
        for i in range(3):
          if enemyBlock[i]==0:
            enemyHp[i] -= attack
          else:
            preAttack = attack
            attack -= enemyBlock[i]
            enemyBlock[i] -= preAttack
            if enemyBlock[i]<=0:
              enemyHp[i] -= attack
            attack = preAttack
      elif randomAttack:
        target = random.randint(1,3)
        for i in range(attackTimes):
          if enemyBlock[(target-1)]==0:
            enemyHp[(target-1)] -= attack
          else:
            preAttack = attack
            attack -= enemyBlock[(target-1)]
            enemyBlock[(target-1)] -= preAttack
            if enemyBlock[(target-1)]<=0:
              enemyHp[(target-1)] -= attack
      energy -= cost
      if not playerTurn:
        for i in cards:
          if i=='Dazed' or i=='Void':
            exhaustPile.append(i)
          if len(exhaustPile) >= 10:
            exhaustPile = []
          else:
            discardPile.append(i)
      if enemyHp[0]<=0 and enemyHp[1]<=0 and enemyHp[2]<=0:
        encounterEnd = True
        encounterWon = True
        encounter += 1
    enemyBlockNew = [0,0,0]
    enemyAttack = 0
    for i in range(3):
      print()
      if enemyHp[i]>0:
        if enemyAction[i]==1:
          enemyAttack = 5
          if shield==0:
            print('Player takes',enemyAttack,'damage')
            hp -= enemyAttack
          else:
            print('Player blocks',enemyAttack,'damage')
            enemyAttack -= shield
            shield -= 5
            if shield<=0:
              print('Player takes',enemyAttack,'damage')
              hp -= enemyAttack
        elif enemyAction[i]==2:
          print('Enemies gain 5 block')
          for e in range(3):
            enemyBlockNew[e] += 5
        elif enemyAction[i]==3:
          print('Player gains 3 Dazed Cards')
          for e in range(3):
            discardPile.append('Dazed')
        elif enemyAction[i]==4:
          print('Player gains 1 Void Card')  
          discardPile.append('Void')
        elif enemyAction[i]==5:
          enemyAttack = 1
          if shield==0:
            print('Player takes',enemyAttack,'damage')
            hp -= enemyAttack
          else:
            print('Player blocks',enemyAttack,'damage')
            enemyAttack -= shield
            shield -= 1
            if shield<=0:
              print('Player takes',enemyAttack,'damage')
              hp -= enemyAttack
        elif enemyAction[i]==6:
          print('Enemies gain 10 block')
          for e in range(3):
            enemyBlockNew[e] += 10
        elif enemyAction[i]==7:
          enemyAttack = 100
          if not enemyBlock[i]<=0:
            if shield==0:
              print('Player takes',enemyAttack,'damage')
              hp -= enemyAttack
            else:
              print('Player blocks',enemyAttack,'damage')
              enemyAttack -= shield
              shield -= 100
              if shield<=0:
                print('Player takes',enemyAttack,'damage')
                hp -= enemyAttack
      else:
        enemyHp[i] = 0
    enemyBlock = enemyBlockNew[::]
    input()
os.system('clear')
if hp<=0:
  print('You Lose')
else:
  print("You Win")