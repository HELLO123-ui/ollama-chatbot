from django.shortcuts import render
from django.http import JsonResponse
import ollama

def chat_page(request):
    # Renders the HTML page for chatting
    return render(request, 'ollama_chat/chat.html')

def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('message', '')
        if not user_input.strip():
            return JsonResponse({'response': "Please enter a valid message."})

        try:
            response = ollama.chat(
                model='phi3:mini',
                messages=[{"role": "user", "content": user_input}]
            )
            reply = response.get('message', {}).get('content', 'No response received.')
        except Exception as e:
            reply = f"❌ Error: {str(e)}"

        return JsonResponse({'response': reply})
    else:
        return JsonResponse({'response': "Only POST method is supported."})
