import os

# 버전별로 상이한 Import 경로를 모두 체크합니다.
try:
    # 1순위: 최신 표준 경로
    from langchain_tavily import TavilySearchResults
except ImportError:
    try:
        # 2순위: 이전 커뮤니티 경로
        from langchain_community.tools.tavily_search import TavilySearchResults
    except ImportError:
        # 3순위: 특정 버전의 하위 경로
        from langchain_tavily.tools import TavilySearchResults

class SearchTool:
    def __init__(self):
        # Tavily API Key
        os.environ["TAVILY_API_KEY"] = "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"
        try:
            # 결과 개수를 5개로 제한
            self.tool = TavilySearchResults(max_results=5)
            self.enabled = True
        except Exception as e:
            print(f"Search Tool 초기화 에러: {e}")
            self.enabled = False

    def run(self, location, query, vibe):
        if not self.enabled: 
            return "Search tool is not configured."
            
        refined_query = f"Top 5 {query} in {location} with {vibe} vibe, specific names only"
        
        try:
            # 최신 LangChain 표준인 invoke() 사용
            return self.tool.invoke(refined_query)
        except AttributeError:
            # 구버전일 경우 run() 사용
            return self.tool.run(refined_query)