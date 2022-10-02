import os
import random, time

class Hangman:

  random.seed(time.time())
  
  def __init__(self, file_name:str=None) -> None:
    #
    self.file_name = file_name if file_name else list(filter(lambda x: x.endswith('txt'), list(os.walk(os.getcwd()))[0][-1]))[0]
    with open(self.file_name, 'r') as file:
      #
      self.words = str(file.read()).split()
    
    print(f'Arquivo de palavras utilizado no jogo: {self.file_name}\n')

    #
    self.hanged_man = [' +---+\n |   |\n     |\n     |\n     |\n     |\n=========', ' +---+\n |   |\n O   |\n     |\n     |\n     |\n=========', ' +---+\n |   |\n O   |\n |   |\n     |\n     |\n=========', ' +---+\n |   |\n O   |\n/|   |\n     |\n     |\n=========', ' +---+\n |   |\n O   |\n/|\\  |\n     |\n     |\n=========', ' +---+\n |   |\n O   |\n/|\\  |\n/    |\n     |\n=========', ' +---+\n |   |\n O   |\n/|\\  |\n/ \\  |\n     |\n=========']
    self.hanged_man_mistakes = len(self.hanged_man)
  

  def show_letters(self, letters:list, message:str=None) -> None:
    if message:
      print(message)
    
    for i in letters:
      print(i)
  

  def read_letter(self) -> str:
    letter = ''
    
    letter = input('Digite uma letra: ')

    #
    if not letter or len(letter) > 1 or (ord(letter.upper()) < ord('A') or ord(letter.upper()) > ord('Z')) and letter.upper() != 'Ç':
      letter = self.read_letter()
    
    return letter
  
  
  def game(self) -> None:
    self.word = random.choice(self.words)
    word_to_guess = ['_' for _ in range(len(self.word))]
    
    wrong_letters, right_letters = [], []

    mistakes = 0

    print('>>>>>>>>>>Hangman<<<<<<<<<<\n')

    while(True):
      print('========================================')
      print('{}\n'.format(self.hanged_man[mistakes]))

      #
      print('Palavra: {}\n'.format(''.join(word_to_guess)))

      self.show_letters(wrong_letters, 'Letras erradas:')

      print()
      self.show_letters(right_letters, 'Letras corretas:')

      print()

      #======================================== :/
      if '_' not in word_to_guess:
        print('Parabéns! Você venceu!!')
        break
      
      elif mistakes == self.hanged_man_mistakes - 1:
        print('Game over! Você perdeu.\nA palavra era {}'.format(self.word))
        break
      #========================================

      letter  = self.read_letter()
      while letter in wrong_letters or letter in right_letters:
        letter  = self.read_letter()
      
      if letter in self.word:
        right_letters.append(letter)

        indexes = [i for i in range(len(self.word)) if self.word[i] == letter]

        for i in indexes:
          word_to_guess[i] = letter
      
      else:
        wrong_letters.append(letter)
        mistakes += 1
    
    print('Foi bom jogar com você! Agora vá estudar!')
    

if __name__ == '__main__':
  hangman = Hangman('words.txt')
  hangman.game()