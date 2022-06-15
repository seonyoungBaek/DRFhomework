# DRFhomework


## mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
mutable은 값이 변하고, immutable은 값이 변하지 않는다.
숫자형 (Number), 문자열 (String), 튜플 (Tuple) -immutable 
리스트 (List), 딕셔너리 (Dictionary) -mutable


## DB Field에서 사용되는 Key 종류와 특징 서술하기
### Primary key(기본 키)
유일무이한 값을 가진 키.  속성이 항상 고유한 값을 가져야 하며, 테이블에 하나만 만들 수 있다.

### Candidate key(후보 키)
기본키의 부분집합. 유일성, 최소성을 만족해야한다.
하나의 키값으로 하나의 튜플만을 유일하게 식별할 수 있어야 하며,
모든 레코드들을 식별하는 데 있어서 꼭 필요한 속성만으로 구성되어 있어야 한다.

### Alternate key(대체 키)
후보키가 둘 이상일 때 기본키를 제외한 나머지 후보키들. 후보키의 부분집합

### Foreign key (외래키)
관련이 있는 여러 테이블들 사이에서 데이터의 일관성을 보장해 주는 수단,
두개의 테이블을 연결해 관계를 맺어주는 기준이 되는 키.


## django에서 queryset과 object는 어떻게 다른지 서술하기
장고에서 .get('key':value)로 데이터를 가져오면 object 형식으로 가져오고, .filter('key':value)로 가져오면 queryset 형식으로 가져온다.
둘의 차이점으로는 object형식은 get 할때 해당 데이터가 없다면 에러가 나지만, queryset형식은 데이터가 존재하지않더라도 빈리스트로 가져와서 정상적으로 작동시킬 수 있다.
때문에 .get 은 try 예외처리를 함께 작성해주어야 데이터가 존재하지 않을 때의 에러를 방지할 수 있다.
