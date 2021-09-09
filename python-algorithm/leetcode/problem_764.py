"""764. Largest Plus Sign
https://leetcode.com/problems/largest-plus-sign/
"""
from functools import lru_cache
from typing import List


class Solution:
    def order_of_largest_plus_sign(self, n: int, mines: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(x: int, y: int, d: int) -> int:
            if (x, y) in zeros:
                return 0
            nx, ny = x + moves[d][0], y + moves[d][1]
            if 0 <= nx < n and 0 <= ny < n:
                return 1 + dfs(nx, ny, d)
            return 1

        def helper(x: int, y: int) -> int:
            cnt = n
            for d in range(4):
                cnt = min(cnt, dfs(x, y, d))
            return cnt

        ans = 0
        zeros = set()
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for zero in mines:
            zeros.add(tuple(zero))
        for i in range(n):
            for j in range(n):
                ret = helper(i, j)
                ans = max(ans, ret)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.order_of_largest_plus_sign(500,
[[0,97],[0,104],[0,318],[0,479],[1,301],[1,417],[1,467],[2,262],[2,470],[3,336],[4,174],[4,330],[4,393],[4,446],[5,126],[5,216],[6,42],[6,213],[6,368],[6,416],[6,441],[6,476],[8,403],[8,483],[9,474],[9,498],[10,135],[10,434],[10,469],[11,72],[11,257],[11,287],[11,497],[12,306],[12,338],[12,361],[12,409],[13,103],[13,418],[13,461],[13,470],[14,21],[14,61],[14,184],[14,338],[14,367],[14,475],[15,50],[15,258],[15,268],[15,446],[15,481],[16,182],[16,333],[17,18],[17,22],[17,205],[17,339],[17,398],[17,486],[18,7],[18,13],[18,197],[18,231],[18,369],[18,412],[19,65],[19,238],[19,241],[19,272],[19,372],[20,111],[20,151],[20,196],[20,219],[20,383],[20,430],[21,34],[21,56],[21,102],[21,157],[21,343],[22,356],[22,483],[23,5],[23,9],[23,256],[23,293],[23,363],[23,381],[23,437],[23,439],[24,12],[24,46],[24,181],[24,192],[25,25],[25,324],[26,127],[26,192],[26,257],[26,432],[27,62],[27,161],[27,175],[27,265],[28,27],[28,54],[28,392],[28,490],[29,45],[29,98],[29,259],[29,292],[29,405],[30,108],[30,361],[30,465],[31,159],[31,237],[31,245],[31,494],[32,19],[32,365],[33,8],[33,115],[33,439],[34,169],[34,250],[34,450],[34,462],[35,26],[35,159],[35,181],[35,253],[36,146],[36,179],[36,326],[36,341],[37,46],[37,116],[37,367],[38,78],[38,169],[38,220],[38,259],[38,372],[38,448],[38,454],[39,35],[39,150],[39,223],[39,266],[39,342],[40,300],[40,409],[40,432],[41,56],[41,119],[41,177],[41,276],[41,318],[41,429],[42,64],[42,90],[42,121],[42,165],[42,173],[42,337],[42,413],[43,136],[43,392],[43,439],[44,5],[44,193],[44,253],[44,378],[45,127],[45,133],[46,139],[46,236],[47,45],[47,77],[47,214],[47,466],[48,70],[48,87],[48,97],[48,152],[48,180],[48,210],[48,328],[48,440],[49,374],[50,27],[50,137],[50,387],[50,447],[51,78],[51,176],[51,244],[51,274],[52,169],[52,233],[52,305],[53,254],[53,364],[54,227],[54,247],[54,264],[54,321],[54,418],[54,449],[54,489],[54,494],[55,251],[55,346],[55,451],[55,470],[56,299],[56,395],[57,203],[57,204],[57,391],[57,420],[57,495],[58,334],[59,87],[59,194],[59,313],[59,336],[59,375],[60,12],[60,25],[60,169],[60,211],[60,225],[60,306],[60,409],[61,67],[61,235],[61,268],[61,271],[62,294],[62,482],[62,485],[63,84],[63,124],[63,442],[63,475],[64,9],[64,405],[64,421],[64,453],[65,206],[65,409],[66,113],[66,234],[66,249],[67,188],[67,190],[67,210],[67,296],[68,98],[68,288],[68,296],[69,165],[70,143],[70,166],[71,465],[72,8],[72,195],[73,394],[73,433],[74,14],[74,60],[74,214],[74,227],[74,323],[74,465],[75,81],[75,117],[75,132],[75,391],[76,149],[76,157],[76,315],[76,324],[76,406],[76,487],[77,46],[77,301],[77,317],[77,318],[77,427],[78,34],[78,51],[78,82],[79,2],[79,206],[79,308],[79,358],[79,379],[80,157],[80,244],[81,193],[81,494],[82,26],[82,30],[82,51],[82,146],[82,245],[83,170],[83,258],[83,307],[83,423],[83,480],[84,125],[84,499],[85,3],[85,216],[85,367],[85,467],[86,109],[86,295],[87,211],[87,245],[87,304],[87,482],[88,3],[88,179],[88,334],[88,342],[88,487],[89,229],[89,239],[89,406],[90,12],[91,90],[91,149],[91,462],[92,115],[93,282],[93,393],[94,19],[94,409],[94,426],[95,14],[95,152],[95,227],[95,293],[96,30],[96,74],[96,141],[96,215],[97,24],[97,129],[97,176],[97,333],[97,459],[97,473],[98,200],[98,219],[98,300],[98,340],[99,36],[99,117],[99,303],[99,422],[100,17],[100,219],[100,232],[100,306],[100,432],[101,84],[101,210],[102,0],[102,16],[102,49],[102,154],[102,227],[102,266],[102,267],[102,370],[102,420],[104,16],[104,134],[104,150],[104,276],[104,324],[104,325],[104,348],[104,478],[105,146],[105,340],[106,196],[106,251],[106,401],[106,411],[106,472],[107,92],[107,283],[107,323],[107,372],[107,431],[108,123],[108,161],[108,249],[108,259],[108,320],[109,23],[109,26],[109,29],[109,103],[109,117],[109,132],[109,153],[109,165],[109,341],[109,429],[110,27],[110,162],[110,194],[110,255],[110,328],[110,342],[111,28],[111,195],[111,278],[111,284],[111,360],[111,377],[111,458],[112,309],[112,456],[113,52],[113,186],[114,69],[114,75],[114,196],[114,398],[114,499],[115,207],[116,36],[116,242],[116,248],[116,292],[116,332],[117,92],[117,215],[117,480],[117,483],[118,105],[118,467],[119,370],[120,16],[120,100],[121,81],[121,306],[122,158],[122,221],[122,246],[122,388],[122,453],[123,76],[123,204],[123,306],[123,489],[124,119],[124,151],[124,194],[124,311],[124,335],[124,401],[125,14],[125,89],[125,114],[125,345],[126,244],[126,403],[127,37],[127,133],[127,153],[127,221],[127,333],[128,32],[128,139],[128,423],[129,94],[129,156],[129,334],[129,383],[129,426],[130,55],[130,207],[130,301],[131,150],[131,345],[132,116],[132,309],[132,311],[133,109],[133,174],[133,234],[134,46],[134,68],[134,442],[135,121],[135,340],[135,489],[136,219],[136,353],[136,374],[137,276],[137,387],[138,69],[138,112],[138,148],[138,203],[138,396],[139,22],[139,164],[139,486],[140,181],[140,190],[140,275],[141,36],[141,254],[141,479],[142,41],[142,212],[142,242],[143,15],[143,56],[143,91],[143,302],[144,35],[144,57],[144,123],[144,228],[144,488],[145,105],[145,279],[146,9],[146,367],[146,417],[147,44],[147,127],[147,372],[148,33],[148,358],[149,8],[149,146],[149,358],[150,53],[150,128],[150,277],[150,304],[151,31],[152,201],[153,7],[153,90],[153,262],[153,474],[154,58],[154,178],[154,371],[154,388],[154,458],[154,497],[155,127],[155,138],[155,340],[156,40],[157,148],[157,278],[157,308],[157,311],[157,368],[157,484],[158,92],[158,102],[158,158],[158,280],[158,303],[158,407],[158,450],[159,37],[159,476],[159,478],[159,483],[160,66],[160,266],[160,309],[160,355],[160,450],[161,43],[161,312],[162,25],[162,92],[162,286],[162,361],[162,372],[162,386],[162,465],[163,56],[163,64],[163,225],[163,246],[163,311],[163,371],[163,428],[164,331],[165,227],[165,427],[165,428],[165,493],[166,331],[166,360],[166,383],[167,10],[167,243],[167,276],[167,403],[168,0],[168,271],[168,286],[168,343],[169,211],[169,418],[169,487],[170,79],[170,126],[171,180],[171,220],[171,303],[171,463],[173,152],[173,156],[173,366],[173,373],[174,59],[174,73],[174,174],[174,495],[175,78],[175,211],[175,421],[176,48],[176,201],[176,386],[176,430],[177,59],[177,306],[178,20],[178,101],[178,119],[178,188],[178,206],[178,347],[178,411],[178,437],[179,93],[179,236],[179,340],[179,354],[179,402],[180,17],[180,108],[180,170],[180,310],[181,50],[181,89],[181,125],[181,182],[181,293],[181,475],[182,1],[182,15],[182,28],[182,242],[182,312],[182,342],[182,445],[183,206],[183,298],[183,456],[184,51],[184,173],[184,274],[184,464],[185,50],[185,137],[185,198],[185,446],[186,15],[186,84],[186,123],[186,210],[186,239],[186,329],[187,463],[188,134],[188,151],[188,337],[188,434],[189,37],[189,211],[190,461],[190,496],[191,184],[191,261],[192,176],[192,262],[192,453],[193,401],[195,17],[195,71],[195,136],[195,142],[195,347],[195,444],[195,494],[196,154],[196,205],[196,238],[196,479],[197,110],[197,149],[197,390],[198,195],[198,305],[199,75],[199,81],[199,193],[199,289],[200,38],[200,235],[200,422],[200,444],[200,448],[200,449],[201,58],[201,68],[201,135],[202,155],[202,375],[202,468],[203,127],[203,207],[203,264],[203,318],[203,387],[203,393],[204,83],[204,179],[204,274],[204,389],[204,441],[204,449],[205,58],[205,319],[205,442],[206,67],[206,204],[206,377],[207,5],[207,20],[207,178],[207,189],[207,192],[207,234],[207,252],[207,441],[208,82],[208,196],[208,249],[208,286],[208,438],[209,101],[209,244],[209,252],[209,261],[209,375],[209,418],[210,75],[210,115],[210,491],[211,73],[211,148],[212,112],[212,209],[212,220],[212,306],[212,345],[212,428],[213,10],[213,73],[213,319],[213,407],[213,478],[214,76],[214,173],[214,332],[214,375],[216,102],[216,421],[216,493],[217,76],[217,150],[217,186],[217,481],[218,150],[219,61],[219,291],[219,351],[219,495],[220,126],[220,136],[220,164],[220,185],[220,382],[220,420],[221,96],[221,392],[222,159],[222,222],[222,359],[222,390],[222,401],[222,409],[223,13],[223,67],[223,119],[223,163],[223,303],[223,304],[223,313],[223,432],[224,3],[224,14],[224,148],[224,162],[224,280],[224,281],[224,291],[224,402],[224,421],[224,457],[225,81],[225,142],[225,184],[225,305],[225,311],[225,373],[226,119],[226,159],[226,234],[226,434],[227,162],[227,173],[227,209],[227,237],[228,104],[228,154],[228,177],[228,249],[228,460],[228,463],[228,465],[229,201],[229,268],[230,21],[230,134],[231,294],[231,300],[231,314],[232,118],[232,255],[232,288],[232,334],[233,296],[233,379],[233,443],[234,170],[234,180],[234,353],[235,1],[235,3],[235,53],[235,70],[235,90],[235,135],[235,208],[235,271],[235,338],[235,429],[236,166],[236,209],[236,283],[236,491],[237,38],[237,221],[237,260],[237,405],[237,472],[237,495],[238,2],[238,166],[238,495],[239,183],[239,305],[239,342],[239,353],[239,399],[240,4],[240,395],[240,440],[241,241],[242,1],[242,134],[242,251],[242,252],[242,273],[242,314],[242,325],[242,349],[242,355],[243,323],[244,30],[245,37],[245,252],[245,451],[246,132],[246,138],[246,213],[247,94],[247,403],[247,453],[248,37],[248,274],[248,486],[249,261],[249,445],[250,80],[250,276],[250,400],[251,160],[251,355],[251,402],[251,458],[251,473],[252,70],[252,76],[252,233],[252,355],[253,132],[253,170],[253,215],[253,263],[253,341],[255,298],[255,447],[256,136],[256,147],[256,222],[256,310],[256,471],[257,132],[257,262],[257,466],[258,6],[258,289],[258,300],[258,397],[258,454],[259,2],[259,267],[260,191],[260,339],[260,476],[261,98],[261,143],[261,151],[261,211],[261,256],[261,302],[262,73],[262,80],[262,245],[262,371],[263,7],[263,114],[263,262],[263,294],[263,374],[263,484],[264,8],[264,238],[264,444],[265,167],[265,225],[266,195],[266,236],[266,434],[266,436],[266,450],[266,458],[267,34],[267,40],[267,77],[267,373],[267,418],[267,435],[267,462],[268,212],[268,328],[268,454],[269,250],[270,192],[270,261],[270,371],[270,404],[271,88],[271,143],[271,249],[271,279],[271,392],[271,400],[272,372],[272,382],[272,417],[273,186],[273,315],[273,320],[274,11],[274,47],[274,56],[274,179],[274,421],[274,468],[275,89],[275,240],[275,290],[275,460],[276,88],[276,256],[276,401],[277,442],[277,444],[278,161],[278,195],[279,77],[279,116],[280,109],[280,132],[280,197],[280,212],[280,230],[280,264],[280,340],[280,365],[280,391],[280,422],[281,153],[281,274],[282,119],[282,397],[282,486],[283,123],[284,12],[284,48],[284,93],[284,125],[284,276],[284,336],[284,428],[285,254],[285,260],[285,397],[285,415],[286,0],[286,60],[286,492],[287,40],[287,72],[287,137],[287,197],[287,288],[287,345],[287,347],[288,63],[288,203],[288,220],[289,231],[289,491],[290,25],[290,160],[290,209],[290,242],[290,285],[292,25],[292,128],[292,447],[293,231],[293,474],[294,70],[294,359],[294,361],[294,371],[294,490],[295,221],[295,346],[296,328],[297,95],[297,222],[297,315],[297,465],[298,129],[298,167],[298,225],[298,350],[298,370],[299,190],[300,345],[300,418],[300,424],[300,482],[301,246],[301,354],[301,499],[302,56],[302,63],[302,144],[302,272],[302,331],[303,98],[303,258],[303,392],[304,6],[304,37],[305,56],[305,233],[305,236],[305,261],[305,312],[305,355],[305,384],[305,394],[306,235],[306,352],[307,283],[307,314],[307,409],[307,422],[308,127],[308,403],[308,453],[309,10],[309,100],[309,101],[309,169],[309,497],[310,43],[310,53],[311,63],[311,74],[311,288],[312,84],[312,144],[312,483],[313,90],[313,189],[313,271],[314,213],[314,258],[314,293],[315,111],[315,286],[315,308],[315,310],[315,360],[315,382],[315,436],[316,42],[317,33],[317,122],[317,223],[317,229],[317,268],[317,307],[317,319],[317,424],[318,38],[318,243],[318,460],[319,89],[319,94],[319,213],[319,239],[319,248],[320,345],[320,377],[321,320],[322,178],[322,266],[322,427],[323,62],[323,168],[323,335],[323,450],[324,112],[324,123],[324,326],[325,59],[325,92],[325,201],[325,223],[325,254],[325,336],[325,350],[326,138],[326,182],[326,296],[327,27],[327,80],[327,137],[327,177],[327,370],[327,451],[328,90],[328,294],[328,460],[329,42],[329,165],[329,251],[329,339],[330,6],[330,101],[330,341],[331,350],[332,184],[332,193],[332,349],[332,385],[332,442],[333,133],[333,198],[333,221],[333,428],[333,454],[334,148],[334,181],[335,164],[335,167],[335,379],[336,2],[336,171],[336,279],[336,345],[336,351],[336,405],[336,465],[337,8],[337,180],[337,252],[337,314],[338,56],[338,220],[338,270],[338,379],[338,460],[339,236],[339,385],[339,405],[339,436],[340,24],[340,46],[340,78],[340,152],[340,199],[341,21],[341,69],[341,133],[342,278],[342,312],[342,419],[342,457],[343,138],[343,216],[343,285],[343,331],[344,38],[344,179],[344,476],[345,42],[345,183],[345,292],[345,383],[345,388],[345,442],[345,454],[346,71],[346,384],[347,374],[347,405],[348,9],[348,84],[348,237],[348,240],[348,313],[348,429],[349,70],[349,199],[349,203],[349,258],[349,427],[350,69],[350,75],[350,475],[350,492],[351,84],[351,419],[352,169],[352,177],[352,309],[352,497],[353,116],[353,125],[353,138],[353,140],[353,191],[354,211],[354,305],[354,373],[354,408],[354,410],[355,32],[355,47],[355,150],[355,239],[355,345],[355,442],[356,17],[356,397],[356,461],[357,96],[357,151],[357,314],[357,334],[357,338],[357,381],[357,479],[358,309],[358,357],[358,365],[359,76],[359,143],[359,171],[359,175],[359,199],[359,287],[360,100],[360,128],[360,174],[360,236],[360,455],[360,480],[361,108],[361,253],[361,379],[361,423],[362,19],[362,89],[362,261],[363,173],[363,266],[363,410],[363,422],[363,468],[364,33],[364,161],[364,412],[365,230],[365,496],[366,36],[366,348],[366,369],[367,54],[367,184],[367,262],[368,113],[368,208],[368,310],[368,350],[369,7],[369,177],[369,396],[370,24],[370,159],[370,249],[370,270],[370,272],[370,411],[371,53],[371,83],[371,112],[371,393],[371,482],[372,122],[372,161],[372,168],[372,262],[372,268],[372,347],[373,196],[373,341],[374,6],[374,75],[374,161],[374,263],[374,360],[374,401],[375,196],[375,322],[376,14],[376,132],[376,168],[376,196],[377,82],[377,239],[377,268],[378,211],[378,287],[379,178],[379,232],[379,442],[379,452],[379,469],[379,475],[380,111],[380,163],[380,346],[380,352],[380,359],[381,181],[381,203],[381,421],[382,89],[382,482],[383,58],[383,215],[383,417],[384,37],[384,200],[384,213],[384,304],[384,498],[385,13],[385,220],[385,325],[385,418],[386,164],[386,171],[386,407],[387,12],[387,302],[388,208],[389,44],[389,87],[390,89],[390,128],[390,206],[390,291],[390,397],[390,465],[391,68],[391,436],[391,489],[392,444],[393,124],[393,131],[393,143],[393,485],[394,13],[394,114],[394,388],[395,92],[395,181],[395,193],[395,335],[396,130],[396,352],[396,368],[397,33],[397,376],[397,386],[398,64],[398,77],[399,212],[399,296],[399,364],[399,425],[399,433],[400,168],[400,252],[401,29],[401,98],[401,105],[401,110],[401,246],[402,196],[402,329],[402,463],[402,470],[403,177],[403,208],[403,283],[403,437],[404,325],[405,30],[405,237],[405,272],[405,282],[406,7],[406,36],[406,286],[406,452],[406,494],[407,272],[407,295],[407,363],[408,320],[408,402],[408,451],[409,114],[409,197],[409,425],[410,237],[410,241],[411,10],[411,25],[411,87],[411,123],[411,175],[411,339],[412,487],[413,91],[413,379],[414,0],[414,251],[414,301],[415,70],[415,341],[415,368],[415,422],[416,88],[416,115],[416,306],[417,121],[417,129],[417,149],[417,286],[417,336],[417,388],[417,483],[418,156],[418,250],[418,371],[418,386],[419,256],[419,427],[420,96],[420,167],[420,196],[420,250],[420,365],[421,115],[421,131],[421,132],[421,234],[421,496],[422,286],[422,418],[423,118],[423,242],[423,264],[423,339],[424,166],[424,222],[424,223],[424,288],[424,290],[425,321],[426,29],[426,147],[426,439],[427,315],[427,352],[428,94],[428,202],[428,228],[428,393],[429,208],[429,236],[429,383],[429,419],[430,29],[430,177],[430,222],[430,274],[430,368],[431,64],[431,345],[432,289],[433,332],[433,383],[434,75],[434,216],[434,262],[434,307],[434,335],[435,36],[435,98],[435,163],[435,265],[435,336],[435,367],[435,416],[435,463],[436,371],[436,493],[437,53],[437,175],[437,231],[437,359],[437,441],[437,444],[438,88],[438,132],[438,379],[438,447],[439,61],[439,249],[439,290],[439,405],[440,142],[440,165],[440,312],[440,472],[441,143],[441,166],[441,182],[441,211],[441,463],[442,124],[442,488],[443,306],[443,424],[443,428],[443,476],[444,167],[444,219],[444,341],[444,351],[444,407],[445,291],[445,330],[445,378],[446,36],[446,179],[446,384],[447,19],[447,76],[447,122],[447,270],[448,73],[448,418],[448,430],[449,26],[449,372],[450,255],[450,262],[451,58],[451,140],[451,214],[451,316],[451,322],[452,35],[452,75],[452,81],[452,120],[452,400],[452,494],[453,45],[453,101],[453,171],[454,172],[454,208],[454,237],[455,24],[455,118],[455,145],[455,216],[455,320],[455,458],[455,473],[456,186],[456,264],[457,112],[457,119],[457,219],[457,232],[457,426],[457,473],[459,38],[459,123],[459,193],[459,252],[460,336],[460,454],[461,121],[461,139],[461,194],[461,222],[461,427],[461,467],[462,67],[463,43],[463,98],[463,117],[463,158],[463,246],[464,10],[464,267],[464,302],[464,361],[465,139],[465,188],[465,414],[466,51],[466,117],[466,150],[466,384],[466,390],[466,445],[467,58],[467,109],[467,136],[467,186],[467,260],[467,287],[467,294],[467,392],[468,146],[468,203],[468,428],[468,451],[469,254],[469,299],[469,307],[470,96],[470,188],[470,472],[471,15],[471,108],[471,163],[471,247],[471,455],[472,2],[472,259],[472,260],[473,98],[473,235],[473,404],[474,122],[474,160],[474,247],[474,298],[474,371],[475,55],[475,62],[475,111],[475,266],[475,289],[475,327],[475,338],[475,443],[475,459],[476,5],[476,51],[476,110],[476,112],[476,158],[476,319],[477,33],[477,91],[477,143],[477,250],[477,254],[477,305],[477,342],[477,428],[478,83],[478,89],[478,257],[479,16],[479,47],[479,78],[479,115],[479,184],[479,345],[480,41],[480,316],[480,326],[480,352],[480,452],[481,80],[481,419],[482,39],[482,108],[482,166],[482,382],[482,420],[483,66],[483,306],[484,143],[484,352],[484,474],[485,14],[485,122],[485,227],[485,269],[486,88],[486,305],[486,378],[487,100],[487,154],[487,174],[487,330],[488,202],[488,342],[489,45],[489,237],[489,410],[489,476],[490,58],[490,164],[490,295],[490,388],[491,21],[491,144],[491,146],[491,447],[492,196],[492,263],[492,268],[492,285],[492,457],[493,31],[493,166],[493,294],[493,301],[494,163],[494,227],[495,84],[495,94],[495,357],[495,461],[496,37],[496,265],[496,434],[497,122],[497,205],[497,493],[498,20],[498,58],[498,88],[498,224],[498,269],[498,302],[498,483],[499,22],[499,303],[499,314],[499,320],[499,322],[499,375]]))
