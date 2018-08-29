import numpy as np
import matplotlib.pyplot as plt


SCORE = np.load('../../dataset/Univ/English/SCORE.npy')
Noftimes = SCORE.shape[1]


def main():
    # get score in Today
    Re_score = int(input('Reading score :'))
    Li_score = int(input('Listening score :'))
    # make new dataset
    new_SCORE = np.zeros((2,Noftimes+1))
    # input score before
    new_SCORE[0,0:Noftimes] = SCORE[0,0:Noftimes]
    new_SCORE[1,0:Noftimes] = SCORE[1,0:Noftimes]
    # input score this time
    new_SCORE[0,Noftimes] = Re_score
    new_SCORE[1,Noftimes] = Li_score
    X = range(1,Noftimes+2,1)
    # plot
    plt.plot(X,new_SCORE[0,:],color='red',label='Reading score')
    plt.plot(X,new_SCORE[1,:],color='blue',label='Listening score')
    plt.xlim(0,Noftimes+3,1)
    plt.ylim(0,30,1)
    plt.legend()
    plt.savefig('../../dataset/Univ/English/TOEFL_score_plot.png')


if __name__ == '__main__':
    main()
