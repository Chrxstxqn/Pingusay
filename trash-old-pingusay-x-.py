import os
 

os.system("clear")

def pingusay(message):
    penguin = r'''
 --------   
| NuT nUt |    __
 -------- -- =(o '.
               '.-.\
               /|  \\
               '|  ||
'''
    os.system("clear")

    bubble = f" {message}\n{penguin}"
    
    os.system("clear")
    
    print(bubble)
    
if __name__ == "__main__":
    user_input = input("Nut Nut?   ") 
    os.system("clear")
    pingusay(user_input)        
          
                    
