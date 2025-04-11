from time import time #to record the time

#now to calculate the accuracy of input prompt
def tperror(prompt):
    global inwords
    words= prompt.split()
    errors=0

    for i in range(len(inwords)):
      if i in range (len(inwords)):
          if inwords[i]==words[i]:
              continue
          else:
              errors=errors+1
      else:
          if inwords[i]==words[i]:
              if(inwords[i+1]==words[i+1]&(inwords[i-1]==words[i-1])):
                  continue
              else:
                  errors+=1
          else:
              errors+=1
      return errors

    #now to calculate the speed of typing words per minute
def speed(inprompt,stime ,etime):
    global time
    global inwords

    inwords=inprompt.split()
    twords=len(inwords)
    speed = twords/time
    return speed
#calculate the total elapsed time
def elapsedtime(stime,etime):  #etime is end of time and stime is start of time
    time=etime-stime
    return time
if  __name__=='__main__':
    prompt="python is interpreted ,high level,general purpose programming langauge created by guido van rossum and first realeased in 1991, python's  desighn philosophy emphasises code of sighnificnt whitespace .its langauge constructs an object-oriented approach aim to help programmers write clear ,logical code for small and large scale projects. python is dynamically typed and garbage collector .it supports multiple programming paradigms including structure (prticularly,procedural). python  iented,and functinal programming . pythnn is often described as a batterise included language due to its comprhensive standard library ."
    #this was a paragraph which you have to typr to check your speed
    print("Type this:-",prompt, " ")
    #checking to input enter basically it will see
    input("press enter when you are ready to check your speed ")

#recording time for input
    stime=time()
    inprompt=input()
    etime =time()

    #collect all the information return by the functions
    time=round(elapsedtime(stime,etime),2)  #round of the time
    speed= speed(inprompt,stime,etime)
    errors=tperror(prompt)

    #printing all the required data to see the results

    print("total time elapsed",time,"seconds")
    print("your average time speed was ",speed,"words per minute (w/m)")
    print("with the total of",errors,"errors")
