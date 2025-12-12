class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        priority_events = []
        
        for event_item in events:
            event_type = event_item[0]
            timestamp = int(event_item[1])
            
            if event_type == 'MESSAGE':
                mentions_string = event_item[2]
                priority_events.append((timestamp, 1, event_type, mentions_string))
            else:
                user_id = int(event_item[2])
                priority_events.append((timestamp, 0, event_type, user_id))
        
        priority_events.sort()
        
        mentions = [0] * numberOfUsers
        online_status = [True] * numberOfUsers
        offline_timers = {}

        for current_timestamp, priority, event_type, event_data in priority_events:
            users_to_reonline = []
            for user_id, re_online_time in list(offline_timers.items()): 
                if re_online_time <= current_timestamp:
                    users_to_reonline.append(user_id)
                    
            for user_id in users_to_reonline:
                online_status[user_id] = True
                del offline_timers[user_id]

            if event_type == "OFFLINE":
                user_id = event_data
                online_status[user_id] = False
                offline_timers[user_id] = current_timestamp + 60
            
            elif event_type == "MESSAGE":
                mentions_string = event_data
                
                if mentions_string == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif mentions_string == "HERE":
                    for i in range(numberOfUsers):
                        if online_status[i]:
                            mentions[i] += 1
                else:
                    ids_str_list = mentions_string.split()
                    for user_mention_str in ids_str_list:
                        user_id = int(user_mention_str[2:])
                        mentions[user_id] += 1
                        
        return mentions