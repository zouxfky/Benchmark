# document
jq -c ".[]" /opt/benchmark/json/document/concept.json > /opt/benchmark/json/document/concept.jsonl

jq -c ".[]" /opt/benchmark/json/document/course.json > /opt/benchmark/json/document/course.jsonl

jq -c ".[]" /opt/benchmark/json/document/problem.json > /opt/benchmark/json/document/problem.jsonl

jq -c ".[]" /opt/benchmark/json/document/user_video.json > /opt/benchmark/json/document/user_video.jsonl

jq -c ".[]" /opt/benchmark/json/document/video.json > /opt/benchmark/json/document/video.jsonl

# kv
jq -c ".[]" /opt/benchmark/json/kv/course_field.json > /opt/benchmark/json/kv/course_field.jsonl

jq -c ".[]" /opt/benchmark/json/kv/user_course.json > /opt/benchmark/json/kv/user_course.jsonl

jq -c ".[]" /opt/benchmark/json/kv/user_problem.json > /opt/benchmark/json/kv/user_problem.jsonl

# relation
jq -c ".[]" /opt/benchmark/json/relation/comment.json > /opt/benchmark/json/relation/comment.jsonl

jq -c ".[]" /opt/benchmark/json/relation/reply.json > /opt/benchmark/json/relation/reply.jsonl

jq -c ".[]" /opt/benchmark/json/relation/teacher.json > /opt/benchmark/json/relation/teacher.jsonl

jq -c ".[]" /opt/benchmark/json/relation/user.json > /opt/benchmark/json/relation/user.jsonl

# garph
jq -c ".[]" /opt/benchmark/json/graph/comment_concept.json > /opt/benchmark/json/graph/comment_concept.jsonl

jq -c ".[]" /opt/benchmark/json/graph/comment_reply.json > /opt/benchmark/json/graph/comment_reply.jsonl

jq -c ".[]" /opt/benchmark/json/graph/concept_prerequisites.json > /opt/benchmark/json/graph/concept_prerequisites.jsonl

jq -c ".[]" /opt/benchmark/json/graph/course_comment.json > /opt/benchmark/json/graph/course_comment.jsonl

jq -c ".[]" /opt/benchmark/json/graph/course_concept.json > /opt/benchmark/json/graph/course_concept.jsonl

jq -c ".[]" /opt/benchmark/json/graph/course_teacher.json > /opt/benchmark/json/graph/course_teacher.jsonl

jq -c ".[]" /opt/benchmark/json/graph/problem_concept.json > /opt/benchmark/json/graph/problem_concept.jsonl

jq -c ".[]" /opt/benchmark/json/graph/user_comment.json > /opt/benchmark/json/graph/user_comment.jsonl

jq -c ".[]" /opt/benchmark/json/graph/user_reply.json > /opt/benchmark/json/graph/user_reply.jsonl

jq -c ".[]" /opt/benchmark/json/graph/video_concept.json > /opt/benchmark/json/graph/video_concept.jsonl
