def main():

    num_males = int(input("Enter the number of males: "))
    num_females = int(input("Enter the number of females: "))

    total_students = num_males + num_females

    m_perc = (num_males / total_students) * 100
    f_perc = (num_females / total_students) * 100
    print("The total number of students:\t", total_students)
    print("The number of males and females:\t", num_males, "\t", num_females)
    print("The percentage of males and females:")
    print("Male: {:.2f}%".format(m_perc))
    print("Female: {:.2f}%".format(f_perc))
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
