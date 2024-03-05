# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative Hierarchial Clustering merges clusters based on distance, making it more resistant to outliers"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "AHC follows a determanistic process based on distance rather than random centroids like K-means "

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Different dataset characteristics come into play when choosing the most efficient clustering algorithm. Cannot make a blanket statement"

    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "SSE of the clustering generally decreases"

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Cohesion implies closer points, so it stands to reason that when SSE decreases, the clusters are becoming more coherent"

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "An increase in SSB shows the distance between clusters is increasing, increasing seperation"

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Seperation and Cohesion are independent"

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "SSE + BSS = Total Variance, so when one increases the other must decrease by that amount"

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Cohesion and Seperation are independent"

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = False

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = '4 * R^2'

    # type: a string that evaluates to a float
    answers["(b) SSE"] = '4 * (b^2 + (a + R)^2)'

    # type: a string that evaluates to a float
    answers["(c) SSE"] = '5 * R^2'

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Because all centroids are initially in Circle B, and all circles are equidistant, I would expect the centroids to shift towards Circle C given the massive difference in points."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Although one centroud starts in A and two in B, the density of C is enough to potentially pull the rightmost centroid towards C"

    # type: int
    answers["(c) Circle (a)"] = 1

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The distance between A and B to C is enough to deter the movement of the centroids and the density of Circle A is enough to keep it within"

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set(['Group A', 'Group B'])

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Closest Points between two clusters"

    # type: set
    answers["(b)"] = set(['A', 'C'])

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Shortest Distance between fartest points in two clusters"

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set(['B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'])

    # type: set
    answers["(a) boundary"] = set(['D', 'G'])

    # type: set
    answers["(a) noise"] = set(['A', 'H'])

    # type: set
    answers["(b) cluster 1"] = set(['B', 'C', 'D', 'E', 'F', 'G'])

    # type: set
    answers["(b) cluster 2"] = set(['I', 'J', 'L', 'M'])

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set(['B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'L', 'M'])

    # type: set
    answers["(c)-a boundary"] = set(['A', 'H'])

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    # type: set
    answers["(c)-b cluster 2"] = set(['H', 'I', 'J', 'L', 'M'])

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Number of objects per category is most evenly distributed"

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "30,000 water indicates dominant category (homogenous cluster)"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Dark Blue diagonal indicates low distance between points in the same cluster"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The dark red squares in Matrix A indicate a high distance between individual clusters"

    # type: string
    answers["(a) Matrix 2"] = "X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Dark Blue diagonal indicates low distance between points in the cluster"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "The symmetry of Matrix 3 corresponds to the linear dsitribution of the clusters shown in Dataset X"

    # type: string
    answers["(a) Matrix 3"] = "Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Ligher colors in the matrics indicate clusters that are not condense. This notion corresponds most with Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Along nondiagonal entries color intensity changes frequently and seemingly random, indicating irregular spacing between clusters"

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Cluster A is not dense nor uniform as shown by the light color of the dark blue square in Row 1 of Matrix 2"

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Darkest Dark Blue square corresponds to the most condensed cluster, shown in Cluster B of Dataset X, as well as Row 2 of Matrix 2"

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Slightly less Cluster C is indicated by the slightly lighter Dark Blue square of Row 3 in Matrix 2."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "CLuster D is not dense nor uniform as shown by the lightest representation of the color of the dark blue square in Row 4, indicating the most spread out and nonuniform distribution of Dataset X"

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchial', 'overlapping', 'partial']

    # type: list
    answers["(b)"] = ['partitional', 'exclusive', 'complete']

    # type: list
    answers["(c)"] = ['partitional', 'exclusive', 'complete']

    # type: list
    answers["(d)"] = ['hierarchial', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['partial', 'exclusive', 'partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "All students recieve an individual grade that places them in a cluster. Not all students take Data Mining as a course"

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Feature clusters in figure A are not likely to be picked up by DBSCAN given their less dense point distribution. Feature clusters in figure B are likely to be picked up by DBSCAN given their more dense point distribution"

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-mean centroids would over iterations converge towrads the denser areas such as the features for figure B, but would struggle to find the features for figure A"

    # type: string
    answers["(c)"] = "Reverse DBSCAN or hierarchial clustering could be used to find the patterns represented by the nose, eyes and mouth"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
