from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def render_sample_template(request: HttpRequest):
    context = {
        'posts': [
            {
                'content': '<p><b>멋쟁이사자처럼</b>은 2013년 프로그래머 <a href="https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%91%90%ED%9D%AC" title="이두희">이두희</a>가 설립한 프로그래밍 교육 단체이다. 궁극적 목표는 <a href="https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B3%BC%ED%95%99" class="mw-redirect" title="컴퓨터과학">컴퓨터과학</a> 비전공자들도 프로그래밍 기초 지식을 배워 자신만의 웹서비스를 만들어 이를 통해 꿈을 실현할 수 있도록 하는 것이다. <a href="https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%91%90%ED%9D%AC" title="이두희">이두희</a>는 “개발자들과 십여 년 동안 지내면서, 이제는 기술적 장벽 때문에 자신의 뜻을 펼치지 못하는 비전공자들을 도와주고 싶었다.”라며, “이들에게 프로그래밍을 교육시켜 작은 서비스를 여럿 내놓을 것이다."라고 설립 취지를 밝혔다. 일주일에 세번 정기교육이 실시되고 그 밖에도 자율적인 만남을 통해 프로그래밍을 위한 개별 논의가 이뤄진다. 2016년 현재 전국의 국내 대학교 및 미국, 호주, 일본 등 세계 대학에서 1000명을 모집하며, 4기 스폰서로 구글코리아, 아마존 웹서비스가 스폰서로 나서 비용 전액을 부담하고 있다. 무료 오프라인 수업 외에 8주 과정으로 진행되는‘코드스터디’라는 온라인 강좌도 있다.</p>',
                'author': {"name": "김동주"},
                'comments': [
                    {
                        'content': '멋쟁이 사자는 어떤 울음소리를 내나요?',
                        'author': {"name": "이동주"},
                        'replies': [
                            {'content': '어흥~ 입니다.', 'author': {'name': '남궁동주'}}
                        ]
                    }
                ]
            },
            {
                'content': '<p>젤다의 전설::티어스 오브 더 킹덤이 곧 출시됩니다!</p><p>많관부!!</p>',
                'author': {"name": "박동주"},
                'comments': [
                    {
                        'content': '티어스 오브 더 킹덤 발매가 벌써 다음 주...! 두근두근.',
                        'author': {"name": "김동주"},
                        'replies': [
                            {
                                'content': '녹색 옷 입은 애가 젤다죠?',
                                'author': {'name': '제갈동주'}
                            },
                            {
                                'content': '아닙니다 ㅡㅡ.',
                                'author': {'name': '황보동주'}
                            }
                        ],
                    }
                ]
            },
        ]
    }
    return render(request, 'sample.html', context)
