from django.shortcuts import render, redirect
import openai

def ChatbotQuery(message):
    openai.api_key = 'YOUR_API_KEY'
    messages = [{"role": "system", "content": "You are an intelligent assistant."}]
    chat = None  # Default value for chat
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
    else:
        reply = "No message provided"  # Handle case when message is empty
    return reply

def DailyChallengeView(request):
    context = {}
    query = "Write a medium difficulty Python puzzle. Please only start your response with 'Here is the Python puzzle:' "
    solution = "Write the solution code to the last puzzle. Do not include explanation just code. Please only start your response with 'Here is the Python solution:'"
    if request.method == 'POST' and 'generate_puzzle' in request.POST:
        puzzle = ChatbotQuery(query)
        solution = ChatbotQuery(solution)
        context['puzzle'] = puzzle
        context['solution'] = solution

    return render(request, 'dailychallenge/dailychallenge.html', context)
