import { createLazyFileRoute } from '@tanstack/react-router'
import PageContent from '../components/PageContent'
import { Button } from 'antd'
import { useEffect, useState } from 'react';
import axios from 'axios';

export const Route = createLazyFileRoute('/')({
  component: () => {
    const [time, setTime] = useState({
        start_time: '',
        end_time: '',
    });
    const [user, setUser] = useState({
        uid: '',
        name: '',
    });

    useEffect(() => {
      axios.get('/api/global/get')
      .then((res: any) => {
        setTime(res.data)
        // console.log(res.data)
      });
      axios.get('/api/whoami')
        .then((res) => {
          setUser(res.data)
        });
    }, []);


    return (
      <>
      <PageContent>
        <h1> 泰山学堂新生报名系统 </h1>
        <hr />
        <p>{user.uid} - {user.name}</p>
        <p> 报名开始时间： {time.start_time}</p>
        <p> 报名截止时间： {time.end_time}</p>
        <p><Button href='/reg/ready-submit'>我的报名状态</Button></p>
        <Button type='primary' href='/reg/contact-details'> 开始报名 </Button>
      </PageContent>
      </>
    )
  },
})
