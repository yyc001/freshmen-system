import { createFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { useRef } from 'react'
import { Button } from 'antd';
import axios from 'axios';

export const Route = createFileRoute('/help/')({
  component: () => {
    const inputRef = useRef<HTMLInputElement>(null);
    // const inputVal: string = "202022300317";
    return (
      <>
        <PageContent>
          <h1> 帮助页面 </h1>
          <Button href='/help/examples'>证书示例</Button>
          <input ref={inputRef}/>
          <Button onClick={()=>{
            axios.post('/api/login_debug', {uid: inputRef.current?.value})
            .then(() => {
              window.location.href = '/'
            })
            }}>切换账号</Button>
        </PageContent> 
      </>
    )
  },
})