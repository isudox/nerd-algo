class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.store = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.store[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.store:
            if self.store[tokenId] + self.ttl <= currentTime:
                del self.store[tokenId]
            else:
                self.store[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for t in self.store.values():
            if t + self.ttl > currentTime:
                cnt += 1
        return cnt
