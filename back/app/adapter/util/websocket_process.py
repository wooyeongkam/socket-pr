precessed_events = set()

def event_processed(event):
  event_key = f"{event}" # event에 따른 key 생성

  if event_key not in precessed_events: # 이벤트가 실행 중이지 않다면
    precessed_events.add(event_key) # set에 이벤트 추가

    return False # 해당 event가 실행 중이지 않았음

  return True # 해당 event가 실행 중이었음

def remove_processed_event(event):
  event_key = f"{event}"

  if event_key in precessed_events:
    precessed_events.discard(event_key)