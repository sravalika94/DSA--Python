class Solution(object):
    def searchMatrix(self, matrix, target):
      n = len(matrix)
      m = len(matrix[0])

        # Set initial binary search range
      low = 0
      high = n * m - 1

        # Perform binary search
      while low <= high:
            # Calculate middle index
         mid = (low + high) // 2

            # Convert 1D index to 2D indices
         row = mid // m
         col = mid % m

            # Check if target is found
         if matrix[row][col] == target:
            return True
            # Discard left half
         elif matrix[row][col] < target:
            low = mid + 1
            # Discard right half
         else:
            high = mid - 1

        # Target not found
      return False                    


        