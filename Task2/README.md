Firstly, I detected the Robots by Motion Detection using the first frame as reference.
Then, I differentiated the Robots 1 and 2 based on the contour lengths of the contours made by the digit plates. This had to be done manually because the difference between their contour lengths varied. It was done by breaking the video into 3 time frames and then comparing the contour lengths in those time frames.
The time complexity of the algorithm is O(Frames*Contours).
The accuracy was not very good owing to the vastly dynamic contour lengths in both robots' digits.
