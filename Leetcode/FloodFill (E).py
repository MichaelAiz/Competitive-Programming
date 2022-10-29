    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        if image[sr][sc] == color:
            return image
        oldColor = image[sr][sc]
        image[sr][sc] = color
        if sr > 0 and image[sr-1][sc] == oldColor:
            self.floodFill(image, sr-1, sc, color)
        if sr < m-1 and image[sr+1][sc] == oldColor:
            self.floodFill(image, sr+1, sc, color)
        if sc > 0 and image[sr][sc-1] == oldColor:
            self.floodFill(image, sr, sc-1, color)
        if sc < n-1 and image[sr][sc+1] == oldColor:
            self.floodFill(image, sr,sc+1, color)
        return image