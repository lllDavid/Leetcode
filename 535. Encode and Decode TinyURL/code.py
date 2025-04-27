class Codec:
    def __init__(self):
        self.url_map = {}
        self.base_url = "http://tinyurl.com/"
        self.chars = string.ascii_letters + string.digits
        
    def encode(self, longUrl: str) -> str:
        while True:
            key = ''.join(random.choice(self.chars) for _ in range(6))
            short_url = self.base_url + key
            if short_url not in self.url_map:
                self.url_map[short_url] = longUrl
                return short_url
                
    def decode(self, shortUrl: str) -> str:
        return self.url_map.get(shortUrl, "")
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))